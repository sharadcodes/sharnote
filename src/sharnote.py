from pathlib import Path, PurePath
from datetime import datetime, timezone
import json
import sys
import re
import getpass
from sys import platform


def configs(config_default_path, force_flag):
    # SET GLOBAL VARS
    if (force_flag or not Path(config_default_path).exists()):
        if not force_flag:
            print("The directory path for notes is missing")
        tmp_notes_dir = str(input("Please enter directory path for notes: "))
        with open(config_default_path, "w") as tf:
            tf.write(tmp_notes_dir)
    # Directory where note files will be saved
    with open(config_default_path, "r") as tf:
        global NOTES_DIR
        NOTES_DIR = tf.readline()


# CHECK OS
def check_os(flag):
    if platform == "linux" or platform == "linux2":
        configs(f"/home/{getpass.getuser()}/sharnote.cfg", flag)
    elif platform == "win32":
        configs(f"C:/Users/{getpass.getuser()}/sharnote.cfg", flag)


check_os(False)

# Set Paths & Dirs
Path(NOTES_DIR).mkdir(parents=True, exist_ok=True)
NOTES_DIR = Path(NOTES_DIR)


# Get current time
DATETIME = str(datetime.now(timezone.utc))
DATE = datetime.now().strftime('%Y_%m_%d')
# File for saving notes will be saved
FILE_PATH = PurePath(NOTES_DIR, f"note_{DATE}.json")
# Boilerplate
BOILERPLATE = {"notes": []}


def save_note(note):
    notes_data = []
    with open(FILE_PATH, 'r') as f:
        notes_data = json.load(f)
    # append to notes data
    notes_data['notes'].append({"time": DATETIME, "note": note})
    with open(FILE_PATH, 'w') as f:
        json.dump(notes_data, f, indent=True)


def get_notes(target_date):
    y = target_date.split("-")[0]
    m = target_date.split("-")[1]
    d = target_date.split("-")[2]
    if(Path(PurePath(NOTES_DIR, f"note_{y}_{m}_{d}.json")).exists()):
        print(f"###### SHOWING NOTES OF {target_date} ######")
        with open(PurePath(NOTES_DIR, f"note_{y}_{m}_{d}.json"), "r") as f:
            n_data = json.load(f)
            for i in n_data['notes']:
                print(f"{i['time']}\t{i['note']}")
    else:
        print(f"------ No file for the given date {target_date} :( ------")


def search(search_key):
    for i in Path(NOTES_DIR).iterdir():
        if(i.is_file()):
            with open(i) as f:
                for x in json.load(f)['notes']:
                    results = re.findall(f".*{search_key}.*", x['note'])
                    if results:
                        for r in results:
                            print(f"{x['time']}\t{r}")


def helper():
    print("SharNote is a python based note taking utility")
    print("Copyright (C) 2020  Sharad Raj Singh Maurya, GNU GPL v3.0\n")
    print("USAGE:\n")
    print("sharnote --help or sharnote --h                Shows help")
    print("sharnote --today or --t                        Shows notes of today")
    print("sharnote --date or --d YYYY-MM-DD              Shows notes of a particaular date")
    print("sharnote --search or --s \"Some text here\"      Search for a particular string in notes")
    print("sharnote --notesdir or --nd                    Change directory used for storing notes")


def main():
    # Get text from argv
    if len(sys.argv) >= 2 and (sys.argv[1] == "--today" or sys.argv[1] == "--t" or sys.argv[1] == "--date" or sys.argv[1] == "--d" or sys.argv[1] == "--search" or sys.argv[1] == "--s" or sys.argv[1] == "--notesdir" or sys.argv[1] == "--nd" or sys.argv[1] == "--help" or sys.argv[1] == "--h"):
        if sys.argv[1] == "--help" or sys.argv[1] == "--h":
            helper()
        elif sys.argv[1] == "--notesdir" or sys.argv[1] == "--nd":
            check_os(True)
        elif len(sys.argv) == 3 and (sys.argv[1] == "--search" or sys.argv[1] == "--s"):
            if (len(sys.argv) > 3):
                print(
                    "------ sharnote ------\nError!\nSearch string should be inside inverted commas")
                print(
                    "Example:   sharnote --search \"Some text here\"    or    sharnote --s \"Some text here\"")
            else:
                search(sys.argv[2].strip(" "))
        elif sys.argv[1] == "--today" or sys.argv[1] == "--t":
            get_notes(datetime.now().strftime('%Y-%m-%d'))
        elif len(sys.argv) == 3 and (sys.argv[1] == "--date" or sys.argv[1] == "--d"):
            get_notes(sys.argv[2])
        else:
            helper()            
    elif len(sys.argv) >= 2 and len(sys.argv[1]) != 0:
        txt = ""
        for word in sys.argv[1:]:
            txt += f"{word} "
            # Check & create file
            pass
        if (Path(FILE_PATH).exists()):
            save_note(txt)
            print("Note saved :)")
        else:
            tmp_file = open(FILE_PATH, "w")
            json.dump(BOILERPLATE, tmp_file)
            tmp_file.close()
            save_note(txt)
            print("Note saved :)")
    else:
        helper()


if __name__ == "__main__":
    try:
        main()
    except:
        print("------- sharnote -------")
        helper()
