#!/usr/bin/python3
"""Time for an interview!"""
if __name__ == "__main__":
    import requests
    import sys
    req = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(sys.argv[2], sys.argv[1]))
    req_c = req.json()
    for c in req_c[:10]:
        print(c.get('sha'), end=': ')
        print(c.get('commit').get('author').get('name'))
