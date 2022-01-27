#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: simplemachinesforum.py
#
# Part of ‘python-simplemachinesforum’
# Project website: https://github.com/oliver-zehentleitner/python-simplemachinesforum
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Copyright (c) 2019-2022, Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import requests
import re
from bs4 import BeautifulSoup
import time


class SimpleMachinesForumAuth(object):
    """
    Helper class for the SimpleMachienForum class, which handles all authentication (login/logout)
    This must be called upon the completion of every session/operation, since otherwise re-logging in will set a new, but invalid, PHPSESSID cookie
    Logging in and logging out every operation makes them idempotent, which costs more bandwidth/time but is easier then tracking login status/timeouts
    By implementing this class to support 'with', it can just be wrapped around each call to handle all authentication automatically
    """

    def __init__(self, smf, session):
        self.smf_info = smf
        self.session = session
        self.smf_session_id = None
        self.smf_random_input = None
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) '
                                      'Gecko/20100101 Firefox/56.0 Waterfox/56.4'}

    def __enter__(self):
        return self.login()

    def login(self):
        """
        Login to the account
        """
        # set sessions headers
        self.session.headers.update(self.headers)

        # login method
        login_url1 = "index.php?action=login"
        login_url2 = "index.php?action=login2"

        # get auth_key and random input name
        login_page = self.session.get(self.smf_info.smf_url + login_url1)
        self.smf_session_id = login_page.text.split("hashLoginPassword(this, '")[1].split("'")[0]
        self.smf_random_input = login_page.text.split("<input type=\"hidden\" name=\"hash_passwrd\" value=\"\" />"
                                                      "<input type=\"hidden\" name=\"")[1].split("\"")[0]
        # login
        payload = {
            'user': self.smf_info.smf_user,
            'passwrd': self.smf_info.smf_pass,
            'cookielength': -1,
            self.smf_random_input: self.smf_session_id,
        }
        # prevent redirects since a correct response will have one, an incorrect response will just return 200
        response = self.session.post(self.smf_info.smf_url + login_url2, data=payload, allow_redirects=False)

        if response.status_code != 302:
            raise Exception("Unable to login to account\n\n=======\n"+str(response.content))

        return self

    def __exit__(self, type, value, traceback):
        self.logout()

    def logout(self):
        """
        Logout from the account
        """
        get_url = "index.php?action=logout;"+str(self.smf_random_input)+"="+str(self.smf_session_id)
        # prevent redirects since a correct response will have one, an incorrect response will just return 200
        response = self.session.get(self.smf_info.smf_url + get_url, allow_redirects=False)

        # you have to wait 2 seconds between login attempts
        time.sleep(3)
        if response is None or response.status_code!=302:
            raise Exception("Unable to logout of account\n\n=======\n"+str(response.content))


class SimpleMachinesForum(object):
    """
    Python API to SimpleMachinesForum

    :param smf_url: URL to the board
    :type smf_url: str
    :param smf_user: Username for the login
    :type smf_user: str
    :param smf_pass: Password for the login
    :type smf_pass: str

    """
    def __init__(self, smf_url, smf_user, smf_pass):
        self.smf_url = smf_url
        self.smf_user = smf_user
        self.smf_pass = smf_pass
        # to ensure we don't start the bot in a bad state (already logged in), preemptively try to log out
        with requests.session() as session:
            auth = SimpleMachinesForumAuth(self, session)
            try:
                auth.login()
            except Exception:
                pass
            try:
                auth.logout()
            except Exception:
                pass

    def new_topic(self, board, subject, msg, icon="xx", notify=0, lock=0, sticky=0):
        """
        Create a new topic on a remote simple machines forum over the network, all it needs is a
        valid user account to login.

        :param board: The board ID (e.g. '1')
        :type board: int
        :param subject: The subject of the new topic.
        :type subject: str
        :param msg: The body text of the new topic.
        :type msg: str
        :param icon: The topic icon, choose: xx = Standard, thumbup = Thumb Up, thumbdown = Thumb Down, exclamation =
                     Exclamation point, question = Question mark, lamp = Lamp, smiley = Smiley, angry = Angry, cheesy = Cheesy,
                     wink = Wink, grin = Grin, sad = Sad
        :type icon: str
        :param notify: Set notifications (0 = no, 1 = yes)
        :type notify: int
        :param lock: Lock the new topic (0 = no, 1 = yes)
        :type lock: int
        :param sticky: Set sticky (0 = no, 1 = yes)
        :type sticky: int
        :return: True or False
        :rtype: bool

        """

        # start a new topic
        post_url1 = "index.php?action=post;board=" + str(board)
        post_url2 = "index.php?action=post2;start=0;board=" + str(board) + ".0"
        
        with requests.session() as session:
            with SimpleMachinesForumAuth(self, session) as auth:
                try:
                    # get seqnum
                    post_page = session.get(self.smf_url + post_url1)
                    seqnum = post_page.text.split("<input type=\"hidden\" name=\"seqnum\" value=\"")[1].split("\"")[0]
                    # post the post :)
                    payload = {'topic': 0,
                               'subject': str(subject),
                               'icon': str(icon),
                               'sel_face': '',
                               'sel_size': '',
                               'sel_color': '',
                               'message': str(msg),
                               'message_mode': 0,
                               'notify': notify,
                               'lock': lock,
                               'sticky': sticky,
                               'move': 0,
                               'attachment[]': "",
                               'additional_options': 0,
                               str(auth.smf_random_input): str(auth.smf_session_id),
                               'seqnum': str(seqnum)}
                    response = session.post(self.smf_url + post_url2, data=payload)
                    if response:
                        return True
                    else:
                        return False
                except KeyError:
                    return False

    def toggle_sticky(self, topic):
        """
        Given a topic ID, toggle the topic's stickiness.

        :param topic: The topic ID (e.g. '1')
        :type topic: int
        :return: True or False
        :rtype: bool

        """

        post_url = "index.php?action=sticky;topic=" + str(topic) + ".0"
        with requests.session() as session:
            with SimpleMachinesForumAuth(self, session) as auth:
                try:
                    post_url += ";"+str(auth.smf_random_input)+"="+str(auth.smf_session_id)
                    #prevent redirects since a correct response will have one, an incorrect response will just return 200
                    response = session.get(self.smf_url + post_url, allow_redirects=False)
                    if response:
                        return response.status_code==302
                    else:
                        return False
                except KeyError:
                    return False

    def get_topic_id(self, board, subject):
        """
        Given a subject name and board, return the topic id for the matching topic.

        :param board: The board ID (e.g. '1')
        :type board: int
        :param subject: The subject of the existing topic.
        :type subject: str
        :return: the topic's id, or None on error
        :rtype: int

        """

        cur_page = 0
        max_page = 0

        # a login is necessary for reading in case the board is in maintenance mode
        with requests.session() as session:
            with SimpleMachinesForumAuth(self, session) as auth:
                #always check the first page, at minimum
                while True:
                    try:
                        #grab the page
                        get_url = "index.php?board=" + str(board) + "." + str(cur_page) + "00"
                        response = session.get(self.smf_url + get_url)
                        if not response:
                            return None

                        #parse the page
                        soup = BeautifulSoup(str(response.content), 'lxml')
                        
                        #grab the max page number
                        pages = soup.find("div", class_="pagelinks floatleft")
                        navpages = pages.find_all("a", class_="navPages")
                        if len(navpages) > 0:
                            max_page = int(navpages[-1].text) - 1 #subrtact 1 since the url is 0 indexed

                        #look for any topics with matching subject
                        topics = soup.find_all("span", id=re.compile("msg_[0-9]+"))
                        for topic in topics:
                            if subject == topic.find("a").text:
                                topicid = topic.find("a")["href"]
                                topicid = re.search("topic.([0-9]+)", topicid).group(1)
                                return int(topicid)
                            
                        #exit the loop if we've hit the last page
                        cur_page += 1
                        if cur_page > max_page:
                            return None
                    except KeyError:
                        return None
                    except ValueError:
                        return None

    def advanced_search_singlepage(self, soup):
        topics = soup.find_all("div", class_="search_results_posts")
        results = []
        
        # return the list of topic ids
        for topic_elems in topics:
            topic_sub = topic_elems.find("div", class_="topic_details floatleft").find("h5")
            topic_urls = topic_sub.find_all("a")
            topic_urls_filtered = []
            for topic in topic_urls:
                # exclude the threadTag url
                if "class" not in topic.attrs:
                    topic_urls_filtered.append(topic)
            topic_url = topic_urls_filtered[-1]["href"]
            topic_num = re.search("topic.([0-9]+)", topic_url).group(1)
            results.append(int(topic_num))
            
        return results

    def advanced_search(self, boards, search_term, users, min_age, max_age, subject_only):
        """
        Use the advanced search feature, and return the list of matches

        :param boards: The boards to search IDs
        :type boards: array of ints
        :param search_term: The search term to use.
        :type search_term: str
        :param users: The usernames to search for. * is all users
        :type users: array of strings
        :param min_age: Youngest posts in days to search for.
        :type min_age: int
        :param max_age: Oldest posts in days to search for.
        :type max_age: int
        :param subject_only: If to only search by subject. 0 for no, 1 for yes.
        :type subject_only: int
        :return: List of topic ids that match the search
        :rtype: array of ints, or None on error
        """
        
        post_url1 = "index.php?action=search2"
        results = []
        offset = 30 #pages are 30 results at a time
        max_offset = 30
        params = ""

        with requests.session() as session:
            with SimpleMachinesForumAuth(self, session) as auth:
                try:
                    payload = {'advanced': 1,
                               'search': search_term,
                               'searchtype': 1,
                               'userspec': ','.join(users),
                               'sort': 'relevance|desc',
                               'minage': min_age,
                               'maxage': max_age,
                               'all': '',
                               'subject_only': subject_only,
                               'submit': 'Search'}
                    # add all the board id's to the payload
                    for board in boards:
                        payload["brd["+str(board)+"]"] = board

                    # parse the first page
                    response = session.post(self.smf_url + post_url1, data=payload)
                    if not response:
                        return None
                    soup = BeautifulSoup(str(response.content), 'lxml')
                    results += self.advanced_search_singlepage(soup)

                    # get the max offset page and the params
                    pages = soup.find("div", class_="pagesection")
                    navpages = pages.find_all("a", class_="navPages")
                    if len(navpages) > 0:
                        navpage_url = navpages[-1]["href"]
                        max_offset = int(navpage_url[navpage_url.rindex("start=")+6:])
                        params = navpage_url[navpage_url.rindex("params=")+7:navpage_url.rindex(";start=")]

                    # parse the next number of pages
                    while offset < max_offset:
                        get_url1 = post_url1 + ";params=" + params + ";start=" + str(offset)
                        response = session.get(self.smf_url + get_url1)
                        
                        # parse this page
                        soup = BeautifulSoup(str(response.content), 'lxml')
                        results += self.advanced_search_singlepage(soup)
                        
                        offset += 30
                        
                except Exception as e:
                    return None

                return results

    def get_stickied_posts(self, board):
        """
        Given a board, return the topic id for all currently stickied topics

        :param board: The board ID (e.g. '1')
        :type board: int
        :return: the topic ids, or None on error
        :rtype: array of ints/None
        """

        results = []
        
        # a login is necessary for reading in case the board is in maintenance mode
        with requests.session() as session:
            with SimpleMachinesForumAuth(self, session) as auth:
                # only need to check the first page
                try:
                    # grab the page
                    get_url = "index.php?board=" + str(board) + ".0"
                    response = session.get(self.smf_url + get_url)
                    if not response:
                        return None

                    # parse the page
                    soup = BeautifulSoup(str(response.content), 'lxml')
                    
                    # look for any topics marked as sticky
                    topics = soup.find("table", class_="table_grid").find("tbody").find_all("tr")
                    for topic in topics:
                        # ignore the background tr element
                        if "class" in topic.attrs:
                            continue

                        topic_idspan = topic.find("span", id=re.compile("msg_[0-9]+")).find("a")["href"]
                        topic_id = int(re.search("topic.([0-9]+)", topic_idspan).group(1))
                        
                        sticky_regx = re.compile('.*stickybg.*')
                        if topic.find("td", {"class":sticky_regx}) is not None:
                            results.append(topic_id)

                    return results

                except Exception:
                    return None
