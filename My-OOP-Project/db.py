import sqlite3
from datetime import date

def pull_db(name="testdatabase.db"):
    db = sqlite3.connect(name)
    create_table(db)
    return db

def create_table(db):
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
        habit TEXT PRIMARY KEY, 
        description TEXT,
        period TEXT,
        streakgoal REAL,
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS tracker (
        date TEXT, 
        counterName TEXT,
        FOREIGN KEY (counterName) REFERENCES counter(name))
        """) 
        
    db.commit()
        
def insert_habit(db, habit, description, period, streakgoal):
    cursor = db.cursor()
    cursor.execute("INSERT OR IGNORE INTO habits (?, ?, ?, ?)", (habit, description, period, streakgoal))
    db.commit()

def increment_counter(db, habit, event_date):
    cursor = db.connect()
    if not event_date:
        event_date = str(date.today())
    cursor.execute("INSERT INTO habits VALUES (?, ?)", (event_date, habit))
    db.commit()


def read(db, habit, description, period, streakgoal):
    cursor = db.cursor("""SELECT * FROM habits""", (habit, description, period, streakgoal))
    return cursor.fetchall()

def update_streakgoal(db, streakgoal):
    cursor = db.cursor()
    cursor.execute('UPDTAE habits WHERE streakgoal = (?)', (streakgoal))
    db.commit()

def delete_habit(db, habit, description, period, streakgoal):
    cursor = db.cursor()
    cursor.execute("DELETE FROM habits WHERE (?)", (habit, description, period, streakgoal))
    db.commit()

def counter_data(db, habit):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tracker WHERE counterName = (?)", (habit))
    return cursor.fetchall()

def tracked_habits(db, habit):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM habits WHERE habit", (habit))
    return cursor.fetchall()

def tracked_habits_period(db, habit, period):
    cursor = db.cursor()
    cursor.execute("SELECT * FFROM habits WHERE period = (?)", (habit , period))
    return cursor.fetchall()

def habits_same_streak(db):
    cursor = db .couror()
    cursor.execute("SELECT * FROM tracker WHERE counterName = (?)")
    return cursor.fetchone()

def streak_longest(db):
    cursor = db .couror()
    cursor.execute("SELECT * FROM tracker WHERE counterName = (?)")
    return cursor.fetchone()

def streak_longest_spec(db):
    cursor = db .couror()
    cursor.execute("SELECT (?) FROM tracker WHERE counterName = (?)")
    return cursor.fetchone()

def show_peroid(db):
    cursor = db.cursor()
    cursor.execute("SELECT (?) FROM habit WHERE period =(?)")
    return cursor.fetchall()
