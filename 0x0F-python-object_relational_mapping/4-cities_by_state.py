#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    """it will not be executed when imported"""
    mydb = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    myc = mydb.cursor()
    myc.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
             FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
               ON `c`.`state_id` = `s`.`id` \
            ORDER BY `c`.`id`")

    for city in myc.fetchall():
        print(city)
