from typing import NamedTuple


class UserDTO(NamedTuple):

    """Контейнер данных без валидаций для вопросов"""

    id: str
    api_key: str
    username: str
