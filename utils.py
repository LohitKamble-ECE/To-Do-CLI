from enum import IntEnum


class Status(IntEnum):
    OPEN = 0
    PENDING = 1
    COMPLETE = 2
    CANCEL = 3


class Priority(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


def get_status_code(user_input: str) -> int:
    normalized = user_input.strip().upper()

    try:
        return Status[normalized].value
    except KeyError:
        raise ValueError(f"Invalid status: {user_input}")


def get_priority_code(user_input: str) -> int:
    normalized = user_input.strip().upper()

    try:
        return Priority[normalized].value
    except KeyError:
        raise ValueError(f"Invalid priority: {user_input}")


def get_status_string(code: int) -> str:
    return Status(code).name


def get_priority_string(code: int) -> str:
    return Priority(code).name
