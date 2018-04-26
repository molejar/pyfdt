#!/usr/bin/env python

# Copyright 2017 Martin Olejar
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path
from setuptools import setup
from fdt import __version__, __license__, __author__, __contact__


def read_file(name):
    return open(path.join(path.dirname(__file__), name)).read()


setup(
    name='fdt',
    author=__author__,
    version=__version__,
    license=__license__,
    author_email=__contact__,
    url='https://github.com/molejar/pyFDT',
    description='Flattened Device Tree Python Module',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    python_requires='>=3',
    install_requires=['click>=5.0'],
    packages=['fdt'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': [
            'pydtc = fdt.tool:main'
        ],
    }
)
