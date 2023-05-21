from app_service_1.dto.question import QuestionDTO
from app_service_1.repositories.api.jservice import SendRequestJservice
from app_service_1.repositories.db.question import CrudQuestion
from app_service_1.shemas.server_answer import MessageResponse
from app_service_1.uow.abstract_uow import AbstractUnitOfWork
from fastapi.responses import JSONResponse


class QuestionUOW(AbstractUnitOfWork):
    """
    Единый класс для работы с моделью вопросов
    """

    def __init__(self, questions_int: int, retry: bool = False) -> None:
        self.questions_int = questions_int
        self.retry = retry

    async def get_and_create_question(
        self,
    ) -> tuple[QuestionDTO | list, int] | tuple[JSONResponse, int]:
        """
        Получить новые вопросы и записать уникальные в БД
        """
        if jservice_data := await SendRequestJservice(
            self.questions_int
        )._send_request():
            last_question, exists_id = await CrudQuestion().create_unique_question(
                jservice_data, self.retry
            )
            return last_question, exists_id
        return (
            JSONResponse(
                content=MessageResponse.BAD_RESPONSE_JSERVICE, status_code=400
            ),
            0,
        )
