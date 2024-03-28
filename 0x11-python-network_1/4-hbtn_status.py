#!/usr/bin/python3
"""What's my status? #1"""
import requests


with requests.get('https://alx-intranet.hbtn.io/status') as response:
    res = response.text
print("Body response:")
print("\t- type: {}".format(type(res)))
print("\t- content: {}".format(res))
