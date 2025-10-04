from rich.console import Console
from rich.table import Table
from utils import get_priority_string
from utils import get_status_string


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

    try:
        for task in tasks:
            table.add_row(
                str(task["id"]),
                task["title"],
                task["due"],
                get_priority_string(task["priority"]),
                get_status_string(task["status"]),
            )
    except Exception:
        table.add_row(
            str(task["id"]),
            task["title"],
            task["due"],
            get_priority_string(task["priority"]),
            get_status_string(task["status"]),
        )

    console.print(table)
