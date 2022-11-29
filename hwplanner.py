from datetime import datetime as dt
from datetime import date
import json

class Color:
    Red = "\033[031m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[96m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightPurple = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"
    Warn = "\033[93m"
    Underline = "\033[4m"
    Bold = "\033[1m"
    Hidden = "\033[8m"
    Blink = "\033[5m"
    Dim = "\033[2m"
    Reverse = "\033[7m"
    Reset = "\033[0m"
    Test = "\033[80m"

def make_a():
    with open("art.txt", "a") as f:
        task = {}

        teacher = input("Enter teacher: ")
        task["teacher"] = teacher

        date = input("Enter due date (mm-dd): ")
        date = dt.strptime(date, "%y-%m-%d")
        date = date.strftime('%A %d %B %Y')
        # date = dt.date(date)
        task["due date"] = str(date)

        print(date)
        desc = input("Enter description: ")
        task["desc"] = desc
        task = json.dumps(task)
        
        f.write(f"{task}\n")

def show_a():
    with open("art.txt", "r") as f:
                
        file_length = f.readlines()
        length = len(file_length)
        f.close()

    with open("art.txt", "r") as f:
        for i in range(length):
            content = f.readline()
            data = json.loads(content)

            print()
            print(f"{Color.LightRed}{json.dumps(data, indent=2)}{Color.Reset}")
            print()

def clear_a():
    open('art.txt', 'w').close()

def make_c():
    with open("cs.txt", "a") as f:
        task = {}

        teacher = input("Enter teacher: ")
        task["teacher"] = teacher

        date = input("Enter due date (mm-dd): ")
        date = dt.strptime(date, "%y-%m-%d")
        date = date.strftime('%A %d %B %Y')
        # date = dt.date(date)
        task["due date"] = str(date)

        print(date)
        desc = input("Enter description: ")
        task["desc"] = desc
        task = json.dumps(task)
        
        f.write(f"{task}\n")

def show_c():
    with open("cs.txt", "r") as f:
                
        file_length = f.readlines()
        length = len(file_length)
        f.close()

    with open("cs.txt", "r") as f:
        for i in range(length):
            content = f.readline()
            data = json.loads(content)

            print()
            print(f"{Color.LightMagenta}{json.dumps(data, indent=2)}{Color.Reset}")
            print()

def clear_c():
    open('cs.txt', 'w').close()

def make_s():
    with open("spanish.txt", "a") as f:
        task = {}

        teacher = input("Enter teacher: ")
        task["teacher"] = teacher

        date = input("Enter due date (mm-dd): ")
        date = dt.strptime(date, "%y-%m-%d")
        date = date.strftime('%A %d %B %Y')
        # date = dt.date(date)
        task["due date"] = str(date)

        print(date)
        desc = input("Enter description: ")
        task["desc"] = desc
        task = json.dumps(task)
        
        f.write(f"{task}\n")
        
def show_s():
    with open("spanish.txt", "r") as f:
                
        file_length = f.readlines()
        length = len(file_length)
        f.close()

    with open("spanish.txt", "r") as f:
        for i in range(length):
            content = f.readline()
            data = json.loads(content)
            
            print()
            print(f"{Color.LightCyan}{json.dumps(data, indent=2)}{Color.Reset}")
            print()

def clear_s():
    open('spanish.txt', 'w').close()

def today():
    time = dt.now().strftime("%H:%M:%S")
    print(f"Today is {Color.LightYellow}{date.today().strftime('%A %d %B %Y')}{Color.Reset} {Color.LightCyan}at{Color.Reset} {Color.LightYellow}{time}{Color.Reset}")

def main():
    while True:

        command = input("What do you want to do? (\"help\" for commands) ").lower()
        
        if command == "make a":
            print()
            make_a()
            print()
        elif command == "show a":
            print()
            show_a()
            print()
        elif command == "clear a":
            clear_a()
        elif command == "make c":
            print()
            make_c()
            print()
        elif command == "show c":
            print()
            show_c()
            print()
        elif command == "clear c":
            clear_c()
        elif command == "make s":
            print()
            make_s()
            print()
        elif command == "show s":
            print()
            show_s()
            print()
        elif command == "clear s":
            clear_s()
        elif command == "show all":
            print()
            show_a()
            print()
            show_c()
            print()
            show_s()
        elif command == "clear all":
            clear_a()
            clear_c()
            clear_s()
        elif command == "today":
            today()
        elif command == "help":
            print(f"""COMMANDS:
        "{Color.LightYellow}make{Color.Reset} {Color.LightPurple}(a, c, s){Color.Reset}" - Allows you to create homework of specified letter (in brackets)

        "{Color.LightYellow}show{Color.Reset} {Color.LightPurple}(a, c, s){Color.Reset}" - Prints all homework of specified letter (in brackets)
        "{Color.LightYellow}show all{Color.Reset}" - Prints all homework
        
        "{Color.LightYellow}clear{Color.Reset} {Color.LightPurple}(a, c, s){Color.Reset}" - Deletes contents of file of specified letter (in brackets)
        "{Color.LightYellow}clear all{Color.Reset}" - Deletes contents of all files

        "{Color.LightYellow}today{Color.Reset}" - Tells you today's date
        "{Color.LightYellow}done{Color.Reset}" - Quits the application
            """)
        elif command == "done":
            
            break
        else:
            print(f"\'{command}\' is not a supported command.")

if __name__ == '__main__':
    main()
