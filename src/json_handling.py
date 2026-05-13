"""Gerencia as Operações com os arquivos JSON"""

from rich import print as bprint
import json

def overwrite_activities(data: list, filename: str) -> None:
    """Sobreescreve as atividades.
       Evita duplicação de dados e má formatação de JSON.

    Args:
        data: A lista com os dados atuais
        filename: O Nome do arquivo JSON
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def save_activity(activity: dict, filename: str) -> None:
    """Salva a atividade

    Args:
        activity: A atividade a salvar
        filename: Nome do arquivo

    Returns:
        None se a atividade estiver vazia
    """

    if activity is None:
        return None

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # lista vazia se não existir

    activity["status"] = "TODO"  # status padrão: TODO
    activity["id"] = len(data)  # id autoincrementa (1, 2, ... N)

    data.append(activity)
    overwrite_activities(data, filename)


def delete_activity(id_to_delete: int, filename: str) -> bool:
    """Deleta a atividade pelo seu ID

    Args:
        id_to_delete: o id da atividade a ser deletada
        filename: Nome do arquivo

    Returns:
        False se o id for menor que 0 ou ocorrer algum erro
        True se conseguir deletar

    Raises:
        IndexError se o id estiver fora do alcance

    """

    if id_to_delete < 0:
        return False

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return False

    try:
        data.pop(id_to_delete)
        overwrite_activities(data, filename)

    # ao tentar deletar uma tarefa de id que não existe...
    except IndexError:
        return False

    return True


def change_status(id_to_change: int, new_status: str, filename: str) -> None:
    """Troca o status de uma tarefa

    Args:
        id_to_change: o id da tarefa a alterar
        new_status: o novo status da tarefa
        filename: o nome do arquivo
    """

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        if item.get("id") == id_to_change:
            item["status"] = new_status
            break  # quebra após encontrar o id pra evitar mais iteracoes

    overwrite_activities(data, filename)


def show_activities(filename: str, *, _detailed: bool = True) -> None:
    """
    exibe todas as atividades

    Args:
        filename: nome do arquivo JSON a ler

    dev Args:
        _detailed:
          se True, mostra informações detalhadas (padrão)
          se False, mostra informações resumidas
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    for item in data:
        bprint()
        bprint(f"[green]Activity[/]: [yellow]{item.get('activity')}[/]")
        bprint(f"[green]ID[/]: {item.get('id')}")

        if _detailed:
            bprint(f"[green]Type[/]: [yellow]{item.get('type')}[/]")
            bprint(
                f"[green]Participants[/]: [yellow]{item.get('participants')}[/]"
            )

        if item.get("link"):
            bprint(f"[green]Link[/]: [yellow]{item.get('link')}[/]")

        bprint(f"[green]Status[/]: [yellow]{item.get('status')}[/]")

    return True
