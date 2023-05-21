import json

import httpx
from app_service_1.dto.question import QuestionDTO
from app_service_1.repositories.api.abstract_api_repository import AbstractAPIRepository
from pydantic import ValidationError
from settings.settings import JSERVICE_URL


class SendRequestJservice(AbstractAPIRepository):
    def __init__(self, questions_int: int) -> None:
        self.url = f"{JSERVICE_URL}{questions_int}"

    async def _send_request(self) -> list[QuestionDTO] | None:
        """
        Функция отправки запроса на API
        """
        async with httpx.AsyncClient() as client:
            response_ = await client.get(url=self.url)
        if response_.status_code == 200:
            return self._parse_response(response_)
        return None

    def _parse_response(
        self, jservice_response: httpx.Response
    ) -> list[QuestionDTO] | None:
        """
        Функция парсинга ответа от API
        """
        question_list = []
        valid_data = []
        try:
            question_list = json.loads(jservice_response.text)
        except json.JSONDecodeError:
            return None
        if question_list:
            for question in question_list:
                try:
                    valid_data.append(QuestionDTO(**question))
                except ValidationError:
                    return None
        if valid_data:
            return valid_data
        return None
