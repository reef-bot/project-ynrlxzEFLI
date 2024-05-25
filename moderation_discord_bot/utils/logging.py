# logging.py

import sqlite3
from datetime import datetime

class Logging:
    def __init__(self, db_file):
        self.db_file = db_file
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS moderation_logs
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      action TEXT,
                      user_id INTEGER,
                      moderator_id INTEGER,
                      timestamp TEXT)''')
        conn.commit()
        conn.close()

    def log_action(self, action, user_id, moderator_id):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute('''INSERT INTO moderation_logs (action, user_id, moderator_id, timestamp)
                     VALUES (?, ?, ?, ?)''', (action, user_id, moderator_id, timestamp))
        conn.commit()
        conn.close()

    def get_logs(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''SELECT * FROM moderation_logs''')
        logs = c.fetchall()
        conn.close()
        return logs

# End of logging.py