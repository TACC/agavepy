"""Serialize a pem file to base-64 encoded values that can be embedded in a CI job
"""

import os
import argparse
import json
import base64

parser = argparse.ArgumentParser()
parser.add_argument("pem_file")
args = parser.parse_args()

def b64encode(data):
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    return encodedStr

with open(args.pem_file) as priv:
	privkey = priv.read()

pubkey_file = args.pem_file + '.pub'
with open(pubkey_file) as publ:
	pubkey = publ.read()

print('TEST_TAPIS_PUBKEY')
print(b64encode(pubkey))
print('TEST_TAPIS_PRIVKEY')
print(b64encode(privkey))
