# db.py
import sqlite3

def init_db():
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chats
                 (session_id TEXT, 
                  question TEXT, 
                  answer TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

def save_chat(session_id, question, answer, timestamp):
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute("INSERT INTO chats VALUES (?, ?, ?, ?)", (session_id, question, answer, timestamp))
    conn.commit()
    conn.close()

def get_chat_history(session_id):
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    c.execute("SELECT question, answer, timestamp FROM chats WHERE session_id = ?", (session_id,))
    rows = c.fetchall()
    conn.close()
    return rows
