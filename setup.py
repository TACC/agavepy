#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand

import os
import sys

HERE = os.path.dirname(__file__)


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--ignore', 'build']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
requires = [pkg for pkg in open('requirements.txt').readlines()]

# append the python2 requirements
if sys.version_info[0] == 2:
    requires.extend([pkg for pkg in open('requirements-py2.txt').readlines()])

data_files = [('', ['requirements.txt', 'requirements-py2.txt'])]

setup(
    name='agavepy',
    version='1.0.0a4',
    description='SDK for TACC Tapis (formerly Agave)',
    long_description=readme,
    author='Texas Advanced Computing Center',
    author_email='jstubbs@tacc.utexas.edu, vaughn@tacc.utexas.edu',
    url='https://github.com/TACC/agavepy',
    packages=[
        'agavepy',
        'agavepy.interactive',
        'agavepy.swaggerpy',
        'agavepy.settings',
        'agavepy.tenants'
    ],
    package_dir={'agavepy': 'agavepy'},
    package_data={'agavepy': [
        'resources.json', 'resources.json.j2', 'resource_exceptions.json', 'resources/*.j2']},
    data_files=data_files,
    install_requires=requires,
    license="BSD",
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'

    ],
    cmdclass={'test': PyTest},
    tests_require=['pytest'],
    test_suite='tests',
)
