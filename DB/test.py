import os
import sqlite3 as sq

with sq.connect("saper.db") as con:

    cur = con.cursor() #Cursor

    #cur.execute("DROP TABLE users") = for at slette schemaet fra db
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER 
    )""")