# To-Do CLI

A simple command-line To-Do application built with Python, [Typer](https://typer.tiangolo.com/), and [Rich](https://rich.readthedocs.io/).

## Features
- Add tasks with title, due date, priority, and status
- Remove tasks by ID
- Remove all tasks
- Update task details
- Show a specific task
- Show all tasks

## Requirements
- Python 3.7+
- [Typer](https://typer.tiangolo.com/) (install with `pip install typer`)
- [Rich](https://rich.readthedocs.io/) (install with `pip install rich`)

## Usage

Run the CLI:

```bash
python main.py [COMMAND] [OPTIONS]
```

### Commands

- `create` — Add a new task
- `remove` — Remove a task by ID
- `remove-all` — Remove all tasks
- `update` — Update a task's details
- `show` — Show a specific task by ID
- `show-all` — Show all tasks

### Examples

Add a new task:
```bash
python main.py create "Buy groceries" --due "2025-10-05" --priority "high" --status "pending"
```

Show all tasks:
```bash
python main.py show-all
```

Remove a task:
```bash
python main.py remove 1
```

## Project Structure
- `main.py` — CLI entry point and commands
- `database.py` — Database logic
- `render.py` — Output formatting (uses Rich for terminal output)
- `utils.py` — Utility functions
- `tasks.db` — SQLite database file

## License
MIT
