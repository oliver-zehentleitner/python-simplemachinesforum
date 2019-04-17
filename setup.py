#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘python-simplemachinesforum’
# Project website: https://github.com/bithon/python-simplemachinesforum
#
# Author: Oliver Zehentleitner
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

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='python-simplemachinesforum',
     version='0.1.0',
     author="Oliver Zehentleitner",
     scripts=['simplemachinesforum.py'],
     description="Python request API to simplemachinesforum",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT License',
     install_requires=[],
     keywords='simple machines forum, python, new post, create post, simplemachinesforum, api',
     project_urls={
         'Source': 'https://github.com/bithon/python-simplemachinesforum',
         'Wiki': 'https://github.com/bithon/python-simplemachinesforum/wiki',
     },
     packages=setuptools.find_packages(),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "License :: OSI Approved :: MIT License",
         'Intended Audience :: Developers',
         "Operating System :: OS Independent",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)

