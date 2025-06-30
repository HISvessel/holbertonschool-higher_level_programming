#!/usr/bin/python3
"""this script iterates through a states list and
filters by first letter"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
        cursor = db.cursor()
        command = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
        cursor.execute(command)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
