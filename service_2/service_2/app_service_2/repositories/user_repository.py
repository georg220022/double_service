from app_service_2.dto.user import UserDTO
from app_service_2.models import user_
from app_service_2.repositories.abstract.abstract_user_repository import (
    AbstractUserRepository,
)
from app_service_2.shemas.api.v1.shema_api_v1 import RequestUserRegistrationSchema
from app_service_2.shemas.server_answer import ServerMessages
from app_service_2.utils.generate_token import create_token
from app_service_2.utils.generate_user_id import create_user_id
from app_service_2.utils.hash_token import hash_token
from fastapi.responses import JSONResponse
from settings.settings import db_async
from sqlalchemy import insert, select


class UserRepository(AbstractUserRepository):

    """Для работы с пользователями в БД"""

    async def create(self, user_data: RequestUserRegistrationSchema) -> UserDTO:
        """
        Создать пользователя в базе
        """
        row_token = create_token()
        hashed_token = hash_token(row_token.encode("utf-8"))
        new_user_id = create_user_id()
        async with db_async as db:
            create_user_query = insert(user_).values(
                username=user_data.username, token=hashed_token, id=new_user_id
            )
            await db.execute(create_user_query)
            await db.commit()
            return UserDTO(
                id=new_user_id, api_key=row_token, username=user_data.username
            )

    async def get(self, user_id: str) -> UserDTO | JSONResponse:
        """
        Получить пользователя из БД по uuid
        """
        async with db_async as db:
            get_user_query = select(user_).where(user_.c.id == user_id).limit(1)
            user_obj = await db.execute(get_user_query)
            if user_obj := user_obj.fetchone():
                id_, username, hashed_token = user_obj
                return UserDTO(id=id_, api_key=hashed_token, username=username)
            return JSONResponse(ServerMessages.NOT_FOUND_USER, status_code=404)

    async def delete(self) -> None:
        pass
