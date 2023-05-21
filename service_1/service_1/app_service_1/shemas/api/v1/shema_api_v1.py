from datetime import datetime

from pydantic import BaseModel


class EmptyDataSchema(BaseModel):
    """Схема ответа при пустой БД"""

    __root__: list

    class Config:
        strict = False


class RequestQuestionNumSchema(BaseModel):
    """Схема POST запроса для сохранения вопроса в БД из jservice.io"""

    questions_num: int


class ResponseQuestionNumSchema(BaseModel):
    """Схема ответа на POST запрос для сохранения новых вопрсов в БД из jservice.io"""

    id: int
    answer: str
    question: str
    created_at: datetime


class ErrorSchema(BaseModel):
    """Схема ошибки"""

    detail: str
