from db import insert_habit, increment_counter, update_streakgoal, delete_habit

class Counter:
    def __init__(self, habit: str, description: str, period: str, streakgoal: str):
        self.habit = habit
        self.description = description
        self.period = period
        self.streakgoal = streakgoal
        self.count = 0

    '''Counter starts here, stored with name and description!'''

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def store(self, db):
        insert_habit(db, self.habit, self.description, self.period, self.streakgoal)

    def add_event(self, db, date: str = None):
        increment_counter(db, self.name, date)

    def update(self, db):
        update_streakgoal(db, self.streakgoal)

    def delete(self, db):
        delete_habit(db, self.habit, self.description, self.period, self.streakgoal, self.count)
