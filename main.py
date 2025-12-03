from habit import Habit
import storage
from utils import clear_screen, colored

def main():
    clear_screen()
    print(colored("=== Habit Tracker ===", "cyan"))

    while True:
        print("""
1. Add Habit
2. Mark Habit Completed
3. View Habits
4. Remove Habit
5. Exit
        """)

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Habit name: ").strip()
            Habit.add_habit(name)

        elif choice == "2":
            name = input("Which habit did you complete? ").strip()
            Habit.mark_completed(name)

        elif choice == "3":
            Habit.view_habits()

        elif choice == "4":
            name = input("Habit to remove: ").strip()
            Habit.remove_habit(name)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print(colored("Invalid choice", "red"))

if __name__ == "__main__":
    main()
