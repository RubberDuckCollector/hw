import json
from datetime import date
from datetime import datetime as dt

class Color:
    Reset = "\033[0m"
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

def make(subject):

    with open(subject, "a") as f:

        task = {}

        teacher = input("Enter teacher: ")
        task["teacher"] = teacher

        date = input("Enter due date (yy-mm-dd): ")
        date = dt.strptime(date, "%y-%m-%d")
        date = date.strftime('%A %d %B %Y')
        task["due date"] = str(date)

        print(date)
        desc = input("Enter description: ")
        task["desc"] = desc
        task = json.dumps(task)
        
        f.write(f"{task}\n")

def show(subject, colour):

    with open(subject, "r") as f:
                
        file_length = f.readlines()
        length = len(file_length)
        f.close()

    with open(subject, "r") as f:

        for i in range(length):
            content = f.readline()
            data = json.loads(content)

            print()
            print(f"{colour}{json.dumps(data, indent=2)}{Color.Reset}")
            print()

def delete(subject, line_number):

    with open(subject, "r") as file:
        lines = file.readlines()

    with open(subject, "w") as file:
        for i, line in enumerate(lines):
            if i + 1 != line_number:
                file.write(line)

def edit_mode(subject):

    with open(subject, "r") as f:
        tasks = []
        for line in f:
            tasks.append(json.loads(line.strip()))

    def write_task(tasks, subject):
        with open(subject, "w") as f:
            for i in tasks:
                f.write(json.dumps(i) + "\n")

    def edit_task(tasks):
        for i, j in enumerate(tasks):
            print(f"Task {i + 1}:")
            print(f"Teacher: {j['teacher']}")
            print(f"Due date: {j['due date']}")
            print(f"Description: {j['desc']}")
            print("")

            choice = input("Enter 'e' to edit this task, or enter any other key to continue: ").lower().replace(" ", "")
            if choice == 'e':
                teacher = input("Enter teacher: ")
                j["teacher"] = teacher

                date = input("Enter due date (yy-mm-dd): ")
                date = dt.strptime(date, "%y-%m-%d")
                date = date.strftime('%A %d %B %Y')
                j["due date"] = str(date)
                print(date)

                desc = input("Enter description: ")
                j["desc"] = desc
    
    edit_task(tasks)
    write_task(tasks, subject)

def today():
    time = dt.now().strftime("%H:%M:%S")
    print(f"Today is {Color.LightYellow}{date.today().strftime('%A %d %B %Y')}{Color.Reset} {Color.LightCyan}at{Color.Reset} {Color.LightYellow}{time}{Color.Reset}")

def main():

    subjects = f"{Color.LightRed}a{Color.Reset}, {Color.LightMagenta}c{Color.Reset}, {Color.LightCyan}s{Color.Reset}, {Color.LightGreen}o{Color.Reset}"

    while True:

        command = input("What do you want to do? (\"help\" for commands) > ").lower().replace(" ", "")
        
        match command:

            case "make":
                subject = input(f"Make a task from what subject? ({subjects}) > ").lower().replace(" ", "")
                match subject:
                    case "a":
                        make("art.txt")
                    case "c":
                        make("cs.txt")
                    case "s":
                        make("spanish.txt")
                    case "o":
                        make("other.txt")
                    case other:
                        print(f"\n'{Color.Bold}{subject}{Color.Reset}' is not a recognised subject.\n")

            case "show":
                subject = input(f"Show a task from what subject? ({subjects}) > ").lower().replace(" ", "")
                match subject:
                    case "a":
                        print()
                        show("art.txt", Color.LightRed)
                        print()
                    case "c":
                        print()
                        show("cs.txt", Color.LightMagenta)
                        print()
                    case "s":
                        print()
                        show("spanish.txt", Color.LightCyan)
                        print()
                    case "o":
                        print()
                        show("other.txt", Color.LightGreen)
                        print()
                    case other:
                        print(f"\n'{Color.Bold}{subject}{Color.Reset}' is not a recognised subject.\n")

            case "d":
                subject = input(f"Delete a task from what subject? ({subjects}) > ").lower().replace(" ", "")
                match subject:
                    case "a":
                        show("art.txt", Color.LightRed)
                        line_num = int(input("What task do you want to delete? > "))
                        delete("art.txt", line_num)
                    case "c":
                        show("cs.txt", Color.LightMagenta)
                        line_num = int(input("What task do you want to delete? > "))
                        delete("cs.txt", line_num)
                    case "s":
                        show("spanish.txt", Color.LightCyan)
                        line_num = int(input("What task do you want to delete? > "))
                        delete("spanish.txt", line_num)
                    case "o":
                        show("other.txt", Color.LightGreen)
                        line_num = int(input("What task do you want to delete? > "))
                        delete("other.txt", line_num)
                    case other:
                        print(f"\n'{Color.Bold}{subject}{Color.Reset}' is not a recognised subject.\n")

            case "showall":
                print()
                show("art.txt", Color.LightRed)
                print()
                show("cs.txt", Color.LightMagenta)
                print()
                show("spanish.txt", Color.LightCyan)
                print()
                show("other.txt", Color.LightGreen)
                print()

            case "dall":
                open("art.txt", "w").close()
                open("cs.txt", "w").close()
                open("spanish.txt", "w").close()
                open("other.txt", "w").close()

            case "today":
                print()
                today()
                print()

            case "e":
                subject = input(f"Edit tasks from what subject? ({subjects}) > ").lower().replace(" ", "")
                print()
                match subject:
                    case "a":
                        edit_mode("art.txt")
                    case "c":
                        edit_mode("cs.txt")
                    case "s":
                        edit_mode("spanish.txt")
                    case "o":
                        edit_mode("other.txt")
                    case other:
                        print(f"\n'{Color.Bold}{subject}{Color.Reset}' is not a recognised subject.\n")

            case "help":
                print(f"""COMMANDS: ({Color.LightRed}a{Color.Reset} -> art, {Color.LightMagenta}c{Color.Reset} -> computer science, {Color.LightCyan}s{Color.Reset} -> spanish, {Color.LightGreen}o{Color.Reset} -> other tasks.)
            "{Color.LightYellow}make{Color.Reset} {Color.LightPurple}({Color.Reset}{subjects}{Color.LightPurple}){Color.Reset}" - Allows you to create homework of specified letter (in brackets)

            "{Color.LightYellow}show{Color.Reset} {Color.LightPurple}({Color.Reset}{subjects}{Color.LightPurple}){Color.Reset}" - Prints all homework of specified letter (in brackets)
            "{Color.LightYellow}showall{Color.Reset}" - Prints all homework
            
            "{Color.LightYellow}d{Color.Reset} {Color.LightPurple}({Color.Reset}{subjects}{Color.LightPurple}){Color.Reset}" - Allows you to delete a task from a subject (in brackets)
            "{Color.LightYellow}dall{Color.Reset}" - Deletes all tasks

            "{Color.LightYellow}e{Color.Reset} {Color.LightPurple}({Color.Reset}{subjects}{Color.LightPurple}){Color.Reset}" - Allows you to edit tasks from a subject (in brackets)

            "{Color.LightYellow}today{Color.Reset}" - Tells you today's date and time
            "{Color.LightYellow}done{Color.Reset}" - Quits the application""")

            case "done":
                break

            case other:
                print(f"\n\'{Color.Bold}{command}{Color.Reset}\' is not a supported command.\n")

if __name__ == '__main__':
    main()
