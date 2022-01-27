![GitHub release](https://img.shields.io/github/release/oliver-zehentleitner/python-simplemachinesforum.svg) 
![GitHub](https://img.shields.io/github/license/oliver-zehentleitner/python-simplemachinesforum.svg?color=blue) 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/simplemachinesforum.svg) 
![PyPI - Status](https://img.shields.io/pypi/status/simplemachinesforum.svg) 
[![Total alerts](https://img.shields.io/lgtm/alerts/g/oliver-zehentleitner/python-simplemachinesforum.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/oliver-zehentleitner/python-simplemachinesforum/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/oliver-zehentleitner/python-simplemachinesforum.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/oliver-zehentleitner/python-simplemachinesforum/context:python)
![PyPI - yes](https://img.shields.io/badge/PyPI-yes-brightgreen.svg?color=orange) 
![PyPI - Wheel](https://img.shields.io/pypi/wheel/simplemachinesforum.svg?label=PyPI%20wheel&color=orange) 
[![Downloads](https://pepy.tech/badge/simplemachinesforum)](https://pepy.tech/project/simplemachinesforum)
[![Downloads](https://pepy.tech/badge/simplemachinesforum/month)](https://pepy.tech/project/simplemachinesforum)
[![Donations/week](http://img.shields.io/liberapay/receives/oliver-zehentleitner.svg?logo=liberapay)](https://liberapay.com/oliver-zehentleitner/donate)
[![Patrons](http://img.shields.io/liberapay/patrons/oliver-zehentleitner.svg?logo=liberapay")](https://liberapay.com/oliver-zehentleitner/donate)

# python-simplemachinesforum
Python request API to Simple Machines Forum: https://www.simplemachines.org/

## Important
A forum is for humans, please use this piece of software only in combination with YOUR OWN FORUM or by order of the forum owner itself to provide a valuable service. Be aware that bots are not tolerated on most boards and its use will lead to a ban.

## What does it can?
- It can create a new topic with `new_topic()` on a remote simple machines forum over the network, all it needs is a valid user account to login.
- Given a topic ID, toggle the topic's stickiness with `toggle_sticky()`.
- Given a subject name and board, return the topic id for the matching topic with `get_topic_id`.
- Use the advanced search feature, and return the list of matches with `advanced_search()`.
- Given a board, return the topic id for all currently stickied topics with `get_stickied_posts()`.

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

### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/python-simplemachinesforum)](https://github.com/oliver-zehentleitner/python-simplemachinesforum/graphs/contributors)

We ![love](https://raw.githubusercontent.com/oliver-zehentleitner/python-simplemachinesforum/master/images/misc/heart.png) open source!

### Donate
Since you are probably a developer yourself, you will understand very well that the creation of open source software is 
not free - it requires technical knowledge, a lot of time and also financial expenditure.

If you would like to help me to dedicate my time and energy to this project, even small donations are very welcome.

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/oliver-zehentleitner/donate)

[:heart: Sponsor (GitHub)](https://github.com/sponsors/oliver-zehentleitner/)

```
Terra (LUNA, UST, ...): terra1yt34qmmycextztnj9mpt3mnjzqqvl8jtqqq7g9
BTC: 39fS74fvcGnmEk8JUV8bG6P1wkdH29GtsA
DASH: XsRhBuPkXGF9WvifdpkVhTGSmVT4VcuQZ7
ETH: 0x1C15857Bf1E18D122dDd1E536705748aa529fc9C
LTC: LYNzHMFUbee3siyHvNCPaCjqXxjyq8YRGJ
XMR: 85dzsTRh6GRPGVSJoUbFDwAf9uwwAdim1HFpiGshLeKHgj2hVqKtYVPXMZvudioLsuLS1AegkUiQ12jwReRwWcFvF7kDAbF
ZEC: t1WvQMPJMriGWD9qkZGDdE9tTJaawvmsBie
```
## Commercial Support
[![LUCIT](https://www.lucit.tech/files/images/logos/LUCIT-LOGO-TRANS-PLAIN-NEW.png)](https://www.lucit.tech)

***Do you need a developer, operator or consultant?***

Contact [me](https://about.me/oliver-zehentleitner) for a non-binding initial consultation via my company 
[LUCIT](https://www.lucit.tech) from Vienna (Austria) or via [Telegram](https://t.me/LUCIT_OZ).