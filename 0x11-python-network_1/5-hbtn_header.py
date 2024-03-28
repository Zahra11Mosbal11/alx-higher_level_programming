#!/usr/bin/python3
"""Response header value #1"""
if __name__ == "__main__":
    import requests
    import sys
    with requests.get(sys.argv[1]) as response:
        request_id = response.headers.get('X-Request-Id')
    print(request_id)
