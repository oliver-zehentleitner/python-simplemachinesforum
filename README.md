![GitHub release](https://img.shields.io/github/release/bithon/python-simplemachinesforum.svg) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/bithon/python-simplemachinesforum.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/simplemachinesforum.svg) ![PyPI - Status](https://img.shields.io/pypi/status/simplemachinesforum.svg) ![PyPI - yes](https://img.shields.io/badge/PyPI-yes-brightgreen.svg) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/simplemachinesforum.svg) ![GitHub](https://img.shields.io/github/license/bithon/python-simplemachinesforum.svg) 

# python-simplemachinesforum
Python request API to Simple Machines Forum: https://www.simplemachines.org/

## Important
A forum is for humans, please use this piece of software only in combination with YOUR OWNN FORUM or by order of the forum owner itself to provide a valuable service. Be aware that bots are not tolerated on most boards and its use will lead to a ban.

## What does it can?
- It can create a new topic on a remote simple machines forum over the network, all it needs is a valid user account to login.

## Installation
`pip install simplemachinesforum`

https://pypi.org/project/simplemachinesforum/
## How to create a new topic?
```
from simplemachinesforum.simplemachinesforum import SimpleMachinesForum
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

If you report a bug, try first the latest release via [download](https://github.com/bithon/python-simplemachinesforum/releases) 
or with `pip install simplemachinesforum --upgrade`. If the issue still exists, provide the error trace, OS 
and python version and explain how to reproduce the error. A demo script is appreciated.
