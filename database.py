from sqlite3 import connect
from sqlite3 import Row
from pathlib import Path

DB_FILE = Path(r"tasks.db")


def init_db():
    with connect(DB_FILE) as conn:
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due TEXT DEFAULT (DATE('now')),
            priority INTEGER DEFAULT 0,
            status INTEGER DEFAULT 0
        )
        """

        conn.execute(query)


def create_task(title: str, due: str, priority: int, status: int):
    with connect(DB_FILE) as conn:
        query = """
        INSERT INTO tasks (title, due, priority, status)
        VALUES (?, ?, ?, ?)
        """

        conn.execute(query, (title, due, priority, status))


def remove_task(task_id: int):
    with connect(DB_FILE) as conn:
        query = """
        DELETE FROM tasks
        WHERE id = ?
        """

        conn.execute(query, (task_id,))


def remove_all_tasks():
    with connect(DB_FILE) as conn:
        query = """
        DELETE FROM tasks
        """

        conn.execute(query)


def update_title(task_id: int, title: str):
    with connect(DB_FILE) as conn:
        query = """
        UPDATE tasks
        SET title = ?
        WHERE id = ?
        """

        conn.execute(query, (title, task_id))


def update_due(task_id: int, due: str):
    with connect(DB_FILE) as conn:
        query = """
        UPDATE tasks
        SET due = ?
        WHERE id = ?
        """

        conn.execute(query, (due, task_id))


def update_priority(task_id: int, priority: int):
    with connect(DB_FILE) as conn:
        query = """
        UPDATE tasks
        SET priority = ?
        WHERE id = ?
        """

        conn.execute(query, (priority, task_id))


def update_status(task_id: int, status: int):
    with connect(DB_FILE) as conn:
        query = """
        UPDATE tasks
        SET status = ?
        WHERE id = ?
        """

        conn.execute(query, (status, task_id))


def get_task(task_id: int):
    with connect(DB_FILE) as conn:
        query = """
        SELECT *
        FROM tasks
        WHERE id = ?
        """
        conn.row_factory = Row
        return conn.execute(query, (task_id,)).fetchall()


def get_all_tasks():
    with connect(DB_FILE) as conn:
        query = """
        SELECT *
        FROM tasks
        """
        conn.row_factory = Row
        return conn.execute(query).fetchall()
