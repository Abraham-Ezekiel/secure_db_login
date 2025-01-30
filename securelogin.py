import sqlite3

import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS userdata (id INTEGER PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL)""")

username1, password1 = "abdepc1", hashlib.sha256("abpassword1".encode()).hexdigest()
username2, password2 = "abdepc2", hashlib.sha256("abpassword2".encode()).hexdigest()
username3, password3 = "abdepc3", hashlib.sha256("abpassword3".encode()).hexdigest()
username4, password4 = "abdepc4", hashlib.sha256("abpassword4".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()
