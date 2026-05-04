from rich import print
import requests

URL = "https://bored-api.appbrewery.com/random"

def show_menu() -> None:
    menu = [
        "Exit",
        "Generate Activity",
        "Delete Activity",
        "Change Activity Status",
        "Show Activities"
    ]

    print()
    for i, choice in enumerate(menu):
        print(f"{i}. {choice}")

def read_choice() -> int:
    return int(input("\n[INPUT] Type Option: "))

def get_activity() -> dict:
    try:
        response = requests.get(URL)
        response.raise_for_status()

        if not response.content:
            raise ValueError("[red][ERROR][/] Empty response from server.")

        result = response.json()

        return result

    except requests.exceptions.HTTPError as e:
        raise
        return {}

def get_id() -> int:
    return int(input("\n[INPUT] ID: "))

def get_new_status() -> str:
    return input("\n[INPUT] New status (TODO, IN_PROGRESS, DONE): ").strip().upper()
