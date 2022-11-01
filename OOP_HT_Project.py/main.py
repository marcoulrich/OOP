from analyze import calculate_count
import questionary
from db import get_db
from counter import Counter

def cli():
    db = get_db()
    questionary.confirm("Are you ready?").ask()

    stop = False
    while not stop:

        choice = questionary.select(
            "What do you want to do?",
            choices=["create", "increment", "analyze", "exit"]
        ).ask()

        name = questionary.text("Whats the name of your counter?").ask()

        if choice == "create":
            desc = questionary.text("Whats the description of your counter?").ask()
            counter = Counter(name, desc)
            counter.store(db)
        elif choice == "increment":
            counter = Counter(name, "no description")
            counter.increment()
            counter.add_event(db)
        elif choice == "analyze":
            count = calculate_count(db, name)
            print(f"{name} has been incremented {count} times")
        else:
            print("bye!")
            stop = True

if __name__ == '__main__':
    cli()