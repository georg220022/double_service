from uuid import uuid4


def create_user_id() -> str:
    return str(uuid4())
