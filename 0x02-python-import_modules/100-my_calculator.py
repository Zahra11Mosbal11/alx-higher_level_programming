#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    args = len(sys.argv)

    if args != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])

        if op not in ['+', '-', '*', '/']:
            print("{}".format("Unknown operator. Available operators: +, -, * and /"))
            sys.exit(1)
        else:
            if op == '+':
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif op == '-':
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif op == '*':
                print("{} * {} = {}".format(a, b, mul(a, b)))
            elif op == '/':
                print("{} / {} = {}".format(a, b, div(a, b)))
