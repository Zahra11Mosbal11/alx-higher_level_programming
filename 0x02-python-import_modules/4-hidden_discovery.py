#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for nam in sorted(dir(hidden_4)):

        if nam[:2] != '__':
            print("{}".format(nam))
