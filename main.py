import datetime as dt

import typer as t

import database as db
import render as r
import utils as ut

app = t.Typer()


@app.command()
def create(
    title: str = t.Argument(..., help="Title of the task."),
    due: str = t.Option(dt.date.today(), help="Due date for the task (YYYY-MM-DD)."),
    priority: str = t.Option(
        "low", help="Priority of the task (e.g., high, medium, low)."
    ),
    status: str = t.Option(
        "open", help="Status of the task (e.g., open, pending, completed, cancelled)."
    ),
):
    """
    Create a new task.

    Args:
        title (str): Title of the task.
        due (str, optional): Due date for the task.
        priority (str, optional): Priority of the task.
        status (str, optional): Status of the task.
    """
    db.create_task(
        title, due, ut.get_priority_code(priority), ut.get_status_code(status)
    )


@app.command()
def remove(task_id: int = t.Argument(..., help="ID of the task to remove.")):
    """
    Remove a task by its ID.

    Args:
        task_id (int): The ID of the task to remove.
    """
    db.remove_task(task_id)


@app.command()
def remove_all():
    """
    Remove all tasks from the to-do list.
    """
    db.remove_all_tasks()


@app.command()
def update(
    id: int = t.Argument(..., help="ID of the task to update."),
    title: str = t.Option(None, help="New title for the task."),
    due: str = t.Option(None, help="New due date for the task (YYYY-MM-DD)."),
    priority: str = t.Option(None, help="New priority for the task."),
    status: str = t.Option(None, help="New status for the task."),
):
    """
    Update an existing task's details.

    Args:
        id (int): ID of the task to update.
        due (str, optional): New due date.
        priority (str, optional): New priority.
        status (str, optional): New status.
    """
    if title:
        db.update_title(id, title)

    if due:
        db.update_due(id, due)

    if priority:
        db.update_priority(id, ut.get_priority_code(priority))

    if status:
        db.update_status(id, ut.get_status_code(status))


@app.command()
def show(id: int = t.Argument(..., help="ID of the task to show.")):
    """
    Show details of a specific task by its ID.

    Args:
        task_id (int): The ID of the task to display.
    """
    details = db.get_task(id)
    r.print_tasks(details)


@app.command()
def show_all():
    """
    Show all tasks in the to-do list.
    """
    details = db.get_all_tasks()
    r.print_tasks(details)


if __name__ == "__main__":
    db.init_db()
    app()
