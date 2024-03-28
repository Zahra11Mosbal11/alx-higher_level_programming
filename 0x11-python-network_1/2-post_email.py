#!/usr/bin/python3
""" POST an email #0"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    vab = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(vab).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        response_data = response.read().decode('utf-8')
    print(response_data)
