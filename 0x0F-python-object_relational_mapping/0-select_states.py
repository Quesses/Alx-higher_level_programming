#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
     db = MySQLdb.connect(host="3306", user=sys.argv[2], passwd=sys.argv[3], db=sys.argv[4])
     cur = db.cursur()
     cur.execute("SELECT * FROM states")
     rows = cur.fetchall()
     for row in rows:
          print(row)
     cur.close()
     db.close()