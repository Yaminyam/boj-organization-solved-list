import sqlite3


def db_setting(group_id):
    conn = sqlite3.connect(str(group_id)+'_unsolved.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS user(name text PRIMARY KEY, solved int)')
    cur.execute('CREATE TABLE IF NOT EXISTS problem(id int PRIMARY KEY)')

    # cur.execute("INSERT OR REPLACE INTO user (name, solved) VALUES ('siontama', 300)")
    # cur.execute("SELECT solved FROM user WHERE name = 'siontam'")
    conn.commit()
    cur.close()
    conn.close()
