<center><h1>0x0F. Python - Object-relational mapping</h1></center>

This project entails linking two amazing worlds: Databases and Python!

First step is the use of the module MySQLdb to connect to a MySQL database and execute several SQL queries.

Second step uses the module SQLAlchemy, an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
See the difference? Cool, right?

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0. Get all states | [0-select_states.py]() | lists all states from the database hbtn_0e_0_usa |
| 1. Filter states |[1-filter_states.py]() | lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa |
|2. Filter states by user input | [2-my_filter_states.py]() | takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument |
