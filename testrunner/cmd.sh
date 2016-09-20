#!/bin/bash
# cmd.sh for the agavepy_testrunner image

# activate the virtualenv
source /ag/bin/activate

# install requirements
pip install -r /agavepy/requirements.txt

# run the tests
cd /agavepy/agavepy/tests; py.test
