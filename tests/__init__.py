import os

PWD = os.getcwd()
HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
TESTS_DATA = os.path.join(PARENT, 'data')
