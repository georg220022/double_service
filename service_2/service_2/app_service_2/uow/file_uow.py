from app_service_2.repositories.upload_file_repository import FileRepository
from app_service_2.shemas.server_answer import ServerMessages
from app_service_2.uow.abstract.abstract_uow import AbstractUnitOfWork
from app_service_2.utils.check_token import check_api_key
from fastapi.responses import JSONResponse


class FileUow(AbstractUnitOfWork):

    """Для работы с репозиториями файлов"""

    def __init__(self) -> None:
        self.file_repo = FileRepository()

    async def create_and_save_mp3(self, user_id, file, api_key) -> JSONResponse:
        """
        Проверяет ключ
        валидирует имя загружаемого файла
        конвертирует
        создает запись о созданном файле в бд
        возвращает ссылку
        """
        if not_valid_key_response := await check_api_key(user_id, api_key):
            return not_valid_key_response
        if bad_name_response := self.file_repo.validator_old_name(file.filename):
            return bad_name_response
        file_name = self.file_repo.convert_to_mp3(file)
        if download_link := await self.file_repo.create_in_db(user_id, file_name):
            return download_link
        return JSONResponse(ServerMessages.ERROR_SAVE_FILE_DB, status_code=400)

    async def get(self, file_name: str) -> JSONResponse:
        """
        Получить файл по имени
        """
        return await self.file_repo.download_file(file_name)
