import storage
from datetime import datetime
from utils import colored

class Habit:

    @staticmethod
    def add_habit(name):
        data = storage.load_data()

        for h in data["habits"]:
            if h["name"].lower() == name.lower():
                print(colored("Habit already exists!", "red"))
                return

        new_habit = {
            "name": name,
            "streak": 0,
            "last_done": None,
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }

        data["habits"].append(new_habit)
        storage.save_data(data)

        print(colored(f"Added '{name}'!", "green"))

    @staticmethod
    def mark_completed(name):
        data = storage.load_data()
        today = datetime.now().strftime("%Y-%m-%d")

        for h in data["habits"]:
            if h["name"].lower() == name.lower():
                if h["last_done"] == today:
                    print(colored("Already marked today!", "yellow"))
                    return

                # Handle streak logic
                if h["last_done"]:
                    last_date = datetime.strptime(h["last_done"], "%Y-%m-%d")
                    gap = (datetime.now() - last_date).days

                    if gap == 1:
                        h["streak"] += 1
                    elif gap > 1:
                        h["streak"] = 1
                else:
                    h["streak"] = 1

                h["last_done"] = today
                storage.save_data(data)
                print(colored(f"Marked '{name}' completed!", "green"))
                return

        print(colored("Habit not found!", "red"))

    @staticmethod
    def view_habits():
        data = storage.load_data()

        if not data["habits"]:
            print(colored("No habits found.", "yellow"))
            return

        print(colored("\nYour Habits:", "cyan"))
        print("-" * 40)
        for h in data["habits"]:
            print(
                f"{h['name']} | Streak: {h['streak']} | Last Done: {h['last_done']}"
            )
        print("-" * 40)

    @staticmethod
    def remove_habit(name):
        data = storage.load_data()

        updated = [h for h in data["habits"] if h["name"].lower() != name.lower()]

        if len(updated) == len(data["habits"]):
            print(colored("Habit not found!", "red"))
            return

        data["habits"] = updated
        storage.save_data(data)
        print(colored(f"Removed '{name}'!", "green"))
