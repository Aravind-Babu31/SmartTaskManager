import sqlite3
import threading

DB_PATH = "taskmanager.db"
lock = threading.Lock()

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

# Create table on module load
with lock:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            day TEXT,
            time TEXT,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_task(task, day, time, category):
    with lock:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (task, day, time, category)
            VALUES (?, ?, ?, ?)
        ''', (task, day, time, category))
        conn.commit()
        conn.close()

def fetch_tasks():
    with lock:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()
        return tasks

