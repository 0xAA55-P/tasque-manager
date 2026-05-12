"""Utilitários Auxiliares"""

from rich import print as bprint
import requests

URL = "https://bored-api.appbrewery.com/random"


def show_menu() -> None:
    menu = [
        "Exit",
        "Generate Activity",
        "Delete Activity",
        "Change Activity Status",
        "Show Activities",
    ]

    bprint()
    for i, choice in enumerate(menu):
        bprint(f"{i}. {choice}")


def read_choice() -> int:
    return int(input("\n[INPUT] Type Option: "))


def get_activity() -> dict | None:
    """Recebe a atividade da API e retorna

    Returns:
        Sucesso: A atividade em formato de dicionário
        Falha: None

    Raises:
        ValueError caso a resposta esteja vazia

    """

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()

        if not response.content:
            raise ValueError("[red][ERROR][/] Empty response from server.")

        result = response.json()

        return result

    except requests.exceptions.HTTPError:
        bprint("\n[yellow][WARNING][/] Request limit exceeded.")
        return None

    except requests.Timeout:
        bprint("\n[yellow][WARNING][/] API took a long time to respond")
        return None


def get_id() -> int:
    return int(input("\n[INPUT] ID: "))


def get_new_status() -> str:
    return input(
        "\n[INPUT] New status (TODO, IN_PROGRESS, DONE): "
    ).strip().upper()
