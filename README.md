![GitHub release](https://img.shields.io/github/release/oliver-zehentleitner/python-simplemachinesforum.svg) 
![GitHub](https://img.shields.io/github/license/oliver-zehentleitner/python-simplemachinesforum.svg?color=blue) 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/simplemachinesforum.svg) 
![PyPI - Status](https://img.shields.io/pypi/status/simplemachinesforum.svg) 
![PyPI - yes](https://img.shields.io/badge/PyPI-yes-brightgreen.svg?color=orange) 
![PyPI - Wheel](https://img.shields.io/pypi/wheel/unicorn-binance-websocket-api.svg?label=PyPI%20wheel&color=orange) 
![PyPI - Downloads](https://img.shields.io/pypi/dm/simplemachinesforum.svg?label=PyPI%20downloads&color=orange)

# python-simplemachinesforum
Python request API to Simple Machines Forum: https://www.simplemachines.org/

## Important
A forum is for humans, please use this piece of software only in combination with YOUR OWN FORUM or by order of the forum owner itself to provide a valuable service. Be aware that bots are not tolerated on most boards and its use will lead to a ban.

## What does it can?
- It can create a new topic on a remote simple machines forum over the network, all it needs is a valid user account to login.

## Installation
`pip install simplemachinesforum`

[https://pypi.org/project/simplemachinesforum/](https://pypi.org/project/simplemachinesforum/)
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

## Documentation
[https://oliver-zehentleitner.github.io/python-simplemachinesforum/](https://oliver-zehentleitner.github.io/python-simplemachinesforum/)

## Project, code and downloads: 
[https://github.com/oliver-zehentleitner/python-simplemachinesforum](https://github.com/oliver-zehentleitner/python-simplemachinesforum)

## Wiki
[https://github.com/oliver-zehentleitner/python-simplemachinesforum/wiki](https://github.com/oliver-zehentleitner/python-simplemachinesforum/wiki)

## How to report bugs or suggest improvements?
Please open a new issue:
[https://github.com/oliver-zehentleitner/python-simplemachinesforum/issues](https://github.com/oliver-zehentleitner/python-simplemachinesforum/issues)

If you report a bug, try first the latest release via [download](https://github.com/oliver-zehentleitner/python-simplemachinesforum/releases) 
or with `pip install simplemachinesforum --upgrade`. If the issue still exists, provide the error trace, OS 
and python version and explain how to reproduce the error. A demo script is appreciated.

## Contributing
`python-simplemachinesforum` is an open source project which welcomes contributions which can be anything from simple 
documentation fixes to new features. To contribute, fork the project on [GitHub](https://github.com/oliver-zehentleitner/python-simplemachinesforum) and send a pull request.
