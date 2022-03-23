#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘python-simplemachinesforum’
# Project website: https://github.com/oliver-zehentleitner/python-simplemachinesforum
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Copyright (c) 2019-2021, Oliver Zehentleitner
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

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='simplemachinesforum',
     version='0.4.4',
     author="Oliver Zehentleitner",
     url="https://github.com/oliver-zehentleitner/python-simplemachinesforum",
     description="Python request API to simplemachinesforum",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT License',
     install_requires=['requests', 'beautifulsoup4'],
     keywords='simple machines forum, python, new post, create post, simplemachinesforum, api',
     project_urls={
         'Wiki': 'https://github.com/oliver-zehentleitner/python-simplemachinesforum/wiki',
         'Documentation': 'https://oliver-zehentleitner.github.io/python-simplemachinesforum',
         'Author': 'https://about.me/oliver-zehentleitner/',
         'Changes': 'https://github.com/oliver-zehentleitner/python-simplemachinesforum/blob/master/CHANGELOG.md',
         'Issue Tracker': 'https://github.com/oliver-zehentleitner/python-simplemachinesforum/issues',
         'Chat': 'https://gitter.im/python-simplemachinesforum/community',
     },
     packages=setuptools.find_packages(),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "License :: OSI Approved :: MIT License",
         'Intended Audience :: Developers',
         "Operating System :: OS Independent",
         "Programming Language :: Python :: 3",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)

