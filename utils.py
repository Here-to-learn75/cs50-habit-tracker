import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def colored(text, color):
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "cyan": Fore.CYAN,
    }
    return colors.get(color, "") + text + Style.RESET_ALL
