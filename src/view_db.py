# view_db.py
import sqlite3

conn = sqlite3.connect("taskmanager.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM tasks")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
