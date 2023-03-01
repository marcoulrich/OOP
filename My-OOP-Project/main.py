import questionary
from db import pull_db 
from counter import Counter 
from analyze import curr_tracked, same_period

def cli():
    db = pull_db()
    questionary.confirm("Do you want to open Habit Tracker?").ask()
    
    stop = False 
    while not stop:
    
        choice = questionary.select(
            "Hello, what do you want to do?",
            choices =["Add Habit", "Manage Habit(s)","Analyze Habit(s)", "Come back tomorrow"]).ask()
        
        if choice == "Add Habit":
            habit = questionary.text("What is the name of your new Habit? ").ask()
            counter = Counter(habit)
            counter.store(db)

            description = questionary.text("Describe your Habit further: ").ask()
            counter = Counter(description)
            counter.store(db)
            
            period = questionary.select(
                "Do you want to do accomplish the Habit daily or each weekly?",
                choices = ["Daily", "Weekly"]).ask()
            if period == "Daily": 
                counter = Counter(period)
                counter.store(db, "Daily")
            else:
                counter = Counter(period)
                counter.store(db, "Weekly")

            
            streakgoal = questionary.text("How often do you want to acomplish your habit?").ask()
            counter = Counter(streakgoal)
            counter.store(db)
            
        elif choice == "Manage Habit(s)":
            choice = questionary.select(
            "Choose your action:",
            choices = ["Update streak for habit", "Change Streakgoal", "Delete habit"]).ask()
            if choice == "Update streak for habit":
                habit = questionary.text("What habit do you want to update?").ask()
                counter = Counter(habit, "no description")
                counter.increment()
                counter.add_event(db)
                #update = questionary.text("What habit(s) did you acomplish today?").ask()


            if choice == "Habit Streakgoal":
                habit = questionary.text("For wich habit do you want to update the streakgoal?").ask()
                counter = Counter(streakgoal)
                counter.update(db)
            

            if choice == "Delete habit":
                habit = questionary.text("Which currently tracked habit do you want to delete?").ask()
                choice = questionary.confirm("Are you sure?").ask()
                stop = False 
                while not stop:
                    counter = Counter(habit)
                    counter.delete(db)
                else:
                    stop = True
                
        elif choice == "Analyze Habit(s)":
            #for item in read(db):
            #    print(item)

            choice = questionary.select(
                "What do you want to inspect?",
            choices = ["Oversee all currently tracked habits", "Habits with the same period", "Habits with same streak", "Longest running streak for specific habit", "Counting longest streak"]).ask()
            
            if choice == "Oversee all currently tracked habits":
                curr_tracked(db)
                return (curr_tracked)
                
            elif choice == "Habits with the same period":
                same_period(db)
                return (same_period)
            
            elif choice == "Habits with same streak":
                pass
            elif choice == "Longest running streak for specific habit":
                pass
            elif choice == "Counting longest streak":
                pass

    else:
        print("Have a wonderful day, until next time!")
        stop = True

if __name__ == '__main__':
    cli()

    