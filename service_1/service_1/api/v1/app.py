from typing import Union

from app_service_1.shemas.api.v1.shema_api_v1 import (
    EmptyDataSchema,
    ErrorSchema,
    RequestQuestionNumSchema,
    ResponseQuestionNumSchema,
)
from app_service_1.tasks_fastapi.background_task import recreate_exists_question
from app_service_1.uow.question_uow import QuestionUOW
from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post(
    "/api/v1/save_new_question",
    status_code=201,
    response_model=Union[ResponseQuestionNumSchema, ErrorSchema, EmptyDataSchema],
)
async def post_question_num(
    request_data: RequestQuestionNumSchema, background_task: BackgroundTasks
) -> JSONResponse:
    """
    Функция получает в теле запроса int сколько вопросов из jservice.io сохранить
    в БД и возвращает 1 последний предыдущий вопрос сохраненный до получения новых
    вопросов.
    """
    last_question, questions_int = await QuestionUOW(
        questions_int=request_data.questions_num
    ).get_and_create_question()
    background_task.add_task(recreate_exists_question, questions_int)
    return last_question
