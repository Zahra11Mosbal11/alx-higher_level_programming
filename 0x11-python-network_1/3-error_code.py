#!/usr/bin/python3
""" Error code """
if __name__ == "__main__":
    import urllib.request
    import sys
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
        print(response_data)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
