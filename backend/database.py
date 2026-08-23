import sqlite3, os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database', 'uzhavan.db')
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS farmers (id INTEGER PRIMARY KEY, name TEXT, crop TEXT)')
    conn.commit()
    conn.close()
if __name__ == "__main__":
    init_db()
    print("DB Created")