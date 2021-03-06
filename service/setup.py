#!/usr/bin/env python
#
# Copyright (c) 2014 ThoughtWorks, Inc.
#
# Pixelated is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pixelated is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Pixelated. If not, see <http://www.gnu.org/licenses/>.

import sys

# next line is a fix to this error that occurs with nose > 1.1.2 and the debian
# python: http://bugs.python.org/issue15881#msg170215
import multiprocessing

import setuptools
from setuptools import setup
from collections import defaultdict
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='pixelated-user-agent',
      version='0.1',
      description='API to serve the pixelated front-end requests',
      long_description=read('README.md'),
      author='Thoughtworks',
      author_email='pixelated-team@thoughtworks.com',
      url='http://pixelated-project.github.io',
      packages=[
          'pixelated',
          'pixelated.adapter',
          'pixelated.adapter.listeners',
          'pixelated.adapter.model',
          'pixelated.adapter.search',
          'pixelated.adapter.services',
          'pixelated.adapter.soledad',
          'pixelated.bitmask_libraries',
          'pixelated.config',
          'pixelated.assets',
          'pixelated.certificates',
          'pixelated.support',
          'pixelated.resources'
      ],
      test_suite='nose.collector',
      install_requires=[
           'pyasn1==0.1.3',
           'gnupg==1.2.5',
           'Twisted==12.0.0',
           'requests==2.0.0',
           'srp==1.0.4',
           'dirspec==4.2.0',
           'u1db==13.09',
           'leap.keymanager==0.3.8',
           'leap.soledad.common==0.6.3',
           'leap.soledad.client==0.6.3',
           'leap.mail==0.3.9-1-gc1f9c92',
           'whoosh==2.5.7'
      ],
      entry_points={
          'console_scripts': [
              'pixelated-user-agent = pixelated.config:initialize'
          ]
      },
      include_package_data=True
)
