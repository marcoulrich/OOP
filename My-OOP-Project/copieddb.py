#import sqlite3
#from datetime import date

#def pull_db(name="database.db"):
#    db = sqlite3.connect(name)
#    return db

#def create_table(db):
#    cursor = db.cursor()

#    cursor.execute("""CREATE TABLE IF NOT EXISTS habit (
#        habitname TEXT PRIMARY KEY, 
#        description TEXT NOT NULL
#        period TEXT NOT NULL,
#        )""")
    
#    cursor.execute("""CREATE TABLE IF NOT EXTISTS track (
#    date TEXT,
#    streakgoal INT NOT NULL
#    )""")

#    db.commit()

#def add_habit(db, name, description):
#   cursor = db.cursor()
#    cursor.execute("INSERT INTO habit VALUES (?, ?)", (name, description))
#   db.commit()

#def update_habit(db, name, start_date):
#    cursor = db.cursor()
#    if not start_date:
#        start_date = str(date.today())
#    cursor.execute("INSERT INTO track VALUES (?, ?)", (start_date, name))
#    db.commit()   

#def update_streakgoal(db, streakgoal):
#    cursor = db.cursor()
#    cursor.execute("UPDATE track SET streakgoal", (streakgoal))
#    db.commit()

#def delete_habit(db):
#    cursor = db.cursor()
#    cursor.execute("DELETE FROM HABIT;")

#def get_data(db, name):
#    cursor = db.execute("SELECT * FROM track WHERE counterName=?", (name,))
#    return cursor.fetchall()
    