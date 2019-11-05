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
# Copyright (c) 2019, Oliver Zehentleitner
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
        self.smf_cookie = False
        self.smf_session_id = False
        self.smf_random_input = False

    def _login(self, session):
        # login method
        login_url1 = "index.php?action=login"
        login_url2 = "index.php?action=login2"
        # get auth_key and random input name
        login_page = session.get(self.smf_url + login_url1)
        self.smf_session_id = login_page.text.split("hashLoginPassword(this, '")[1].split("'")[0]
        self.smf_random_input = login_page.text.split("<input type=\"hidden\" name=\"hash_passwrd\" value=\"\" />"
                                                      "<input type=\"hidden\" name=\"")[1].split("\"")[0]
        # login
        payload = {
            'user': self.smf_user,
            'passwrd': self.smf_pass,
            'cookielength': -1,
            self.smf_random_input: self.smf_session_id,
        }
        response = session.post(self.smf_url + login_url2, data=payload)
        print("Login Response: %s" % response)

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
            self._login(session)
            # get seqnum
            post_page = session.get(self.smf_url + post_url1, cookies=session.cookies)
            try:
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
                           str(self.smf_random_input): str(self.smf_session_id),
                           'seqnum': str(seqnum)}
                response = requests.post(self.smf_url + post_url2, data=payload, cookies=session.cookies)
                if response:
                    return True
                else:
                    return False
            except KeyError:
                return False

