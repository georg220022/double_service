import os
from uuid import uuid4

from app_service_2.models import user_file_
from app_service_2.shemas.server_answer import ServerMessages
from fastapi import UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pydub import AudioSegment
from pydub.exceptions import PydubException
from settings.settings import (
    FORMAT_SONG,
    MAX_LEN_FILE_NAME,
    MIN_LEN_FILE_NAME,
    STORAGE_PATH,
    VALID_FORMAT_UPLOAD,
    db_async,
)
from sqlalchemy import insert


class FileRepository:

    """Для работы с загружаемыми файлами"""

    def create_name_with_format(self) -> str:
        """
        Создает имя из 'uuid4' + '.' + 'формат песни'
        """
        return f"{str(uuid4())}.{FORMAT_SONG}"

    def convert_to_mp3(self, file: UploadFile):
        """
        Конвертирует песню из wav -> mp3
        и сохраняет на диск
        """
        name_file = self.create_name_with_format()
        try:
            file_ = AudioSegment.from_wav(file.file)
            file_.export(f"{STORAGE_PATH}{name_file}", format=FORMAT_SONG)
        except PydubException:
            return JSONResponse(ServerMessages.ERROR_CONVERT, status_code=400)
        return name_file

    def validator_old_name(self, old_name_file) -> bool | JSONResponse:
        """
        Валидация имени загружаемого пользователем файла
        """
        if (
            MIN_LEN_FILE_NAME > len(old_name_file)
            or len(old_name_file) > MAX_LEN_FILE_NAME
        ):
            return JSONResponse(ServerMessages.ERROR_LENGTH_FILE_NAME, status_code=400)
        if (
            old_name_file[len(old_name_file) - len(VALID_FORMAT_UPLOAD) :].lower()
            != VALID_FORMAT_UPLOAD
        ):
            return JSONResponse(ServerMessages.ERROR_FILENAME, status_code=400)
        return False

    async def create_in_db(self, user_id, file_name):
        """
        Создает запись в БД о сконвертированном файле
        """
        async with db_async as db:
            save_file_query = insert(user_file_).values(
                user_id=user_id, file_path=file_name
            )
            await db.execute(save_file_query)
            await db.commit()
            return JSONResponse(
                ServerMessages.DOWNLOAD_LINK["detail"].format(file_name=file_name),
                status_code=201,
            )

    async def download_file(self, file_name: str) -> FileResponse | JSONResponse:
        """
        Отдает файл на скичивание если такой есть в STORAGE_PATH
        """
        if file_name:
            path_file = f"{STORAGE_PATH}{file_name}"
            if os.path.exists(path_file):
                return FileResponse(path=path_file, media_type="audio/mpeg")
        return JSONResponse(ServerMessages.NOT_FOUND_FILE, status_code=404)
