from abc import ABC, abstractmethod

import httpx


class AbstractAPIRepository(ABC):
    """
    Абстрактный класс для всех API репозиториев
    """

    def __init__(self, client: httpx.AsyncClient) -> None:
        self.client = client

    @abstractmethod
    async def _send_request(self, url: str, params=None, body=None):
        """
        Абстрактная функция для отправки запросов на сторонние API
        """
        pass

    @abstractmethod
    async def _parse_response(self, *args, **kwargs):
        """
        Абстрактная функция для парсинга ответов от сторонних API
        """
        pass
