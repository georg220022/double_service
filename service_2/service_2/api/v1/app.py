from typing import Annotated, Union

from app_service_2.repositories.user_repository import UserRepository
from app_service_2.shemas.api.v1.shema_api_v1 import (
    ErrorSchema,
    RequestUserRegistrationSchema,
    ResponseFileSchema,
    ResponseUserRegistrationSchema,
)
from app_service_2.uow.file_uow import FileUow
from fastapi import FastAPI, Form, Header, UploadFile
from fastapi.responses import FileResponse
from pydantic import UUID4

app = FastAPI()


@app.post(
    "/api/v1/registration",
    status_code=201,
    response_model=ResponseUserRegistrationSchema,
)
async def registration_user(request_data: RequestUserRegistrationSchema):
    """
    Регистрация нового пользователя
    """
    return (await UserRepository().create(request_data))._asdict()


@app.post("/api/v1/upload_wav", response_model=Union[ResponseFileSchema, ErrorSchema])
async def create_upload_file(
    file: UploadFile,
    user_id: Annotated[UUID4, Form()],
    api_key: Annotated[str, Header(convert_underscores=False)],
):
    """
    Получает файл от пользователя с api_key в формате .wav
    конвертирует в .mp3
    возвращает ссылку на скачивание
    """
    return await FileUow().create_and_save_mp3(user_id, file, api_key)


@app.get("/download/{file_name}", response_class=FileResponse)
async def download_mp3(file_name):
    """
    Синхронная ручка
    Скачивает файл с указанным названием, доступно без api_key
    """
    return await FileUow().get(file_name)
