"""Um gerador de Tarefas Aleatórias em Python.

Dev: Anna
Github: https://github.com/0xAA55-P
Data de Atualização: 12/05/2026

APIs: Bored API
"""

from rich import print as bprint
from utils import get_id, get_new_status, read_choice, show_menu, get_activity
from json_handling import save_activity, show_activities, change_status, delete_activity

import requests

AVAILABLE_CHOICES = {0, 1, 2, 3, 4}
VALID_STATUS = {"TODO", "IN_PROGRESS", "DONE"}
FILENAME = "../json/activities.json"


def handle_choice(choice: int) -> bool:
    """Trata a escolha do usuário

    Args:
        choice: A escolha

    Returns:
        False se o usuário escolheu sair
        True se a função terminou com sucesso

    Raises:
        ValueError se a escolha estiver fora do alcance de 0-4

    """

    if choice not in AVAILABLE_CHOICES:
        raise ValueError()

    if choice == 0:
        bprint("\n[green][EXIT][/] Goodbye!\n")
        return False

    match choice:
        case 1:
            activity = save_activity(get_activity(), FILENAME) 
            bprint("\n[green][SUCCESS][/] Activity saved successfully.")

        case 2:
            show_activities(FILENAME, _detailed=False)

            print()
            id_to_delete = get_id()

            if delete_activity(id_to_delete - 1, FILENAME):
                bprint("\n[green][SUCCESS][/] Activity deleted.")
            else:
                bprint("\n[red][ERROR][/] Couldn't delete activity.")
                bprint(
                    "[red][ERROR][/] Check if you entered the correct id."
                )

        case 3:
            show_activities(FILENAME, _detailed=False)

            id_to_change = get_id()
            new_status = get_new_status()

            if new_status not in VALID_STATUS:
                bprint("\n[red][ERROR][/] Invalid status.")
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
            bprint("\n[yellow][WARNING][/] Invalid Value.")
        except KeyboardInterrupt:
            bprint("\n[green][EXIT][/] Goodbye!\n")


if __name__ == "__main__":
    main()
