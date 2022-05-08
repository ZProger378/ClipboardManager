import random
import sqlite3
import datetime


def reset_database():
    with open("clipboard_history.db", "w") as f:
        f.write("")
    con = sqlite3.connect("clipboard_history.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE History (id INT, date TEXT, data TEXT)")


def add_record(data):
    con = sqlite3.connect("clipboard_history.db")
    cur = con.cursor()
    dt_now = datetime.datetime.now()
    date_str = dt_now.strftime('%H:%M %d.%m.%Y')
    cur.execute("INSERT INTO History (id, date, data) VALUES (?, ?, ?)",
                (random.randint(100000, 999999), date_str, data))
    con.commit()


def get_records():
    con = sqlite3.connect("clipboard_history.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM History")
    unsorted = cur.fetchall()
    result = []
    for i in unsorted:
        result.append({
            'id': i[0],
            'date': i[1],
            'data': i[2]
        })

    return result


def get_record(record_id):
    con = sqlite3.connect("clipboard_history.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM History WHERE id = ?", (record_id,))
    i = cur.fetchone()
    result = {
            'id': i[0],
            'date': i[1],
            'data': i[2]
        }

    return result


def clear_history():
    con = sqlite3.connect("clipboard_history.db")
    cur = con.cursor()
    cur.execute("DELETE FROM History")
    con.commit()
