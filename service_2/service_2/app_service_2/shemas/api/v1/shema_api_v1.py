from pydantic import BaseModel, Field


class RequestUserRegistrationSchema(BaseModel):
    """Схема POST запроса при регистрации юзера"""

    username: str = Field(min_length=1, max_length=50)


class ResponseUserRegistrationSchema(RequestUserRegistrationSchema):
    """Схема ответа при регистрации юзера"""

    id: str
    api_key: str


class ErrorSchema(BaseModel):
    """Схема ошибки"""

    detail: str


class ResponseFileSchema(ErrorSchema):
    pass
