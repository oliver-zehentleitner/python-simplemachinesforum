# python-simplemachinesforum
Python request API to Simple Machines Forum: https://www.simplemachines.org/

## What does it can?
- It can create a new Topic from a remote server, all it needs is a valid user account to login.

## Installation
`pip install simplemachinesforum`

## How to create a new topic?
```
smf_url = "https://www.any-simplemachinesforum.com"
smf_user = "user_name"
smf_pass = "password"
smf = SimpleMachinesForum(smf_url, smf_user, smf_pass)
# 1 = board id:
smf.new_topic(1, "subject", "This is the message to post!")
```

## Project, code and downloads: 
https://github.com/bithon/python-simplemachinesforum

## Wiki
https://github.com/bithon/python-simplemachinesforum/wiki

## How to report bugs or suggest improvements?
Please open a new issue:
https://github.com/bithon/python-simplemachinesforum/issues

If you report a bug, try first the latest release via [download](https://github.com/unicorn-data-analysis/unicorn-binance-websocket-api/releases) 
or with `pip install python-simplemachinesforum --upgrade`. If the issue still exists, provide the error trace, OS 
and python version and explain how to reproduce the error. A demo script is appreciated.

