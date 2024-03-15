#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    """it will not be executed when imported"""
    mydb = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    myc = mydb.cursor()
    state_name = sys.argv[4]
    myc.execute("SELECT cities.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s", (state_name,))

    print(", ".join(city[0] for city in myc.fetchall()))
