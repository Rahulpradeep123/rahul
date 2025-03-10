import sqlite3
conn = sqlite3.connect("data.db")
print("opened database successfully")
conn.execute("CREATE TABLE registers(username varchar,email varchar,password varchar)")
conn.execute("CREATE TABLE admin(email varchar,password varchar)")
conn.execute("CREATE TABLE raja(fullname varchar,email varchar,date date,nationality varchar,phone number,password varchar,Address varchar,gender varchar)")
print("table created successfully")
conn.close()