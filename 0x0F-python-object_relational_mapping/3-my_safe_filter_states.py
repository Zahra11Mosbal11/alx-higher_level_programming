#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    """it will be calling when in main"""
    mydb = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    myc = mydb.cursor()
    myc.execute("SELECT * FROM `states`")

    for state in myc.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
