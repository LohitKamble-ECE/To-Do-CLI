from rich.console import Console
from rich.table import Table

import utils as ut


def print_tasks(tasks):
    console = Console()

    if not tasks:
        console.print(r"[blue]Empty list. Try creating new task![/blue]")
        return

    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", overflow="fold")
    table.add_column("Due Date", style="blue", no_wrap=True)
    table.add_column("Priority", style="blue", no_wrap=True)
    table.add_column("Status", style="blue", no_wrap=True)

    for task in tasks:
        table.add_row(
            str(task["id"]),
            task["title"],
            task["due"],
            ut.get_priority_string(task["priority"]),
            ut.get_status_string(task["status"]),
        )

    console.print(table)
