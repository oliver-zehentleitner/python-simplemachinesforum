#!/usr/bin/env python

from simplemachinesforum.simplemachinesforum import SimpleMachinesForum

# config
smf_url = "https://www.any-simplemachinesforum.com"
smf_user = "BOT"
smf_pass = ""

# create instance
smf = SimpleMachinesForum(smf_url, smf_user, smf_pass)

# post new topic
smf.new_topic(1, "Subject of test topic:", "This is a test message!")
