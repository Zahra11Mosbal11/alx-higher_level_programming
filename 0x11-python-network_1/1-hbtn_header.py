#!/usr/bin/python3
"""Response header value #0"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    request_id = response.headers.get('X-Request-Id')
print(request_id)
