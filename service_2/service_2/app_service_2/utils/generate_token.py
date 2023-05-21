from uuid import uuid4


def create_token() -> str:
    return str(uuid4())
