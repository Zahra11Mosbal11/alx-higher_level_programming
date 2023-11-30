#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    sum1 = 0
    if args == 1:
        print("{}".format(sum1))
    else:
        for i in range(1, args):
            sum1 += int(sys.argv[i])
        print("{}".format(sum1))
