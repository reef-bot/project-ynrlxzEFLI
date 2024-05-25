# database.py

import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS moderation_actions (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                action TEXT,
                                user_id INTEGER,
                                moderator_id INTEGER,
                                timestamp TEXT
                                )''')
        self.conn.commit()

    def log_moderation_action(self, action, user_id, moderator_id, timestamp):
        self.cursor.execute('''INSERT INTO moderation_actions (action, user_id, moderator_id, timestamp)
                                VALUES (?, ?, ?, ?)''', (action, user_id, moderator_id, timestamp))
        self.conn.commit()

    def get_moderation_logs(self):
        self.cursor.execute('''SELECT * FROM moderation_actions''')
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()