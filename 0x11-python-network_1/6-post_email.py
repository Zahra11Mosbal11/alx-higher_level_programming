#!/usr/bin/python3
""" POST an email #1 """
if __name__ == "__main__":
    import requests
    import sys
    vab = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=vab)
    print(req.text)
