from app_service_2.dto.user import UserDTO
from app_service_2.repositories.user_repository import UserRepository
from app_service_2.shemas.server_answer import ServerMessages
from app_service_2.utils.hash_token import hash_token


async def check_api_key(user_id, api_key) -> ServerMessages | None:
    """
    Берет из БД пользователя
    Хеширует полученный api_key из параметров
    Сверяет уже хешированный ключ из БД с хешированным api_key
    """
    if isinstance(
        user_dto := await UserRepository().get(user_id), UserDTO
    ) and user_dto.api_key == hash_token(api_key.encode("utf-8")):
        return None  # pass
    return ServerMessages.NOT_VALID_USER
