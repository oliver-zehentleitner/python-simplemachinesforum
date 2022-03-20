# python-simplemachinesforum Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).


## 0.4.2.dev (development stage/unreleased)

## 0.4.2
Publishing on conda-forge

## 0.4.1
### Fixed
- 404 images on PyPi.

## 0.4.0
### Added
- Given a topic ID, toggle the topic's stickiness with `toggle_sticky()`. [PR#3](https://github.com/oliver-zehentleitner/python-simplemachinesforum/pull/3) Thanks to [metal-crow](https://github.com/metal-crow)!
- Given a subject name and board, return the topic id for the matching topic with `get_topic_id`. [PR#3](https://github.com/oliver-zehentleitner/python-simplemachinesforum/pull/3) Thanks to [metal-crow](https://github.com/metal-crow)!
- Use the advanced search feature, and return the list of matches with `advanced_search()`. [PR#3](https://github.com/oliver-zehentleitner/python-simplemachinesforum/pull/3) Thanks to [metal-crow](https://github.com/metal-crow)!
- Given a board, return the topic id for all currently stickied topics with `get_stickied_posts()`. [PR#3](https://github.com/oliver-zehentleitner/python-simplemachinesforum/pull/3) Thanks to [metal-crow](https://github.com/metal-crow)!

## 0.3.0
### Added 
- docstrings
- new_topics now returns True or False

## 0.2.0
### Added
- new_topic() support msg_icon, notify, sticky, ...

## 0.1.6
### Fixed
- KeyError

## 0.1.5
- troubles with pypi :)

## 0.1.0
### Added
- _login method
- new_topic method
- github
- pypi
