#!/usr/bin/python3
"""Search API"""
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        req_d = req.json()
        if len(req_d) == 0 or not req_d.get('id') or not req_d.get('name'):
            print("No result")
        else:
            print("[{}] {}".format(req_d.get('id'), req_d.get('name')))
    except ValueError:
        print("Not a valid JSON")
