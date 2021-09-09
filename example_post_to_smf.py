#!/usr/bin/env python

from simplemachinesforum.simplemachinesforum import SimpleMachinesForum
import random

# config
smf_url = "https://s2.demo.opensourcecms.com/smf/"
smf_user = "opensourcecms"
smf_pass = "opensourcecms"

# create instance
smf = SimpleMachinesForum(smf_url, smf_user, smf_pass)

# post new topic
subject = "Subject of test topic:"+str(random.randint(0, 9999))
print("new_topic=" + str(smf.new_topic(1, subject, "This is a test message!")))
topicid = smf.get_topic_id(1, subject)
print("get_topic_id=" + str(topicid))
stickied = smf.toggle_sticky(topicid)
print("toggle_sticky=" + str(stickied))
print("get_stickied_posts=" + str(smf.get_stickied_posts(1)))
print("advanced_search=" + str(smf.advanced_search([1], subject, ["*"], 0, 9999999, 0)))