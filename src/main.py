import requests
import json
from rich import print
from utils import *
from json_handling import *

AVAILABLE_CHOICES = { 0, 1, 2, 3, 4 }
VALID_STATUS = { "TODO", "IN_PROGRESS", "DONE" }
FILENAME = "../json/activities.json"

def handle_choice(choice: int) -> bool:
    if choice not in AVAILABLE_CHOICES:
        raise ValueError()

    if choice == 0:
        print("\n[green][EXIT][/] Goodbye!\n")
        return False

    match choice:
        case 1:
            save_activity(get_activity(), FILENAME)
            print("\n[green][SUCCESS][/] Activity saved successfully.")

        case 2:
            show_activities(FILENAME, _detailed=False)

            print()
            id_to_delete = get_id()

            if delete_activity(id_to_delete, FILENAME):
                print("\n[green][SUCCESS][/] Activity deleted.")
            else:
                print("\n[red][ERROR][/] Couldn't delete activity.")
                print("[red][ERROR][/] Check if the file exists or if you entered the correct id.")

        case 3:
            show_activities(FILENAME, _detailed=False)

            id_to_change = get_id()
            new_status = get_new_status()

            if new_status not in VALID_STATUS:
                print("\n[red][ERROR][/] Invalid status.")
            else:
                change_status(id_to_change, new_status, FILENAME)

        case 4:
            show_activities(FILENAME) 
        
    return True

def main():
    while True:
        try:
            show_menu()
            if not handle_choice(read_choice()):
                break

        except ValueError:
            print("\n[yellow][WARNING][/] Invalid Value.")
        except KeyboardInterrupt:
            print("\n[green][EXIT][/] Goodbye!\n")

if __name__ == "__main__":
    main()
