# custom_settings.py

import sqlite3

class CustomSettings:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS custom_settings (
                                setting_name TEXT PRIMARY KEY,
                                setting_value TEXT
                                )''')
        self.conn.commit()

    def set_setting(self, setting_name, setting_value):
        self.cursor.execute('''INSERT OR REPLACE INTO custom_settings (setting_name, setting_value)
                               VALUES (?, ?)''', (setting_name, setting_value))
        self.conn.commit()

    def get_setting(self, setting_name):
        self.cursor.execute('''SELECT setting_value FROM custom_settings WHERE setting_name = ?''', (setting_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def delete_setting(self, setting_name):
        self.cursor.execute('''DELETE FROM custom_settings WHERE setting_name = ?''', (setting_name,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()