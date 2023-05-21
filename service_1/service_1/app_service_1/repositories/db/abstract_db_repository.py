from abc import ABC, abstractmethod


class AbstractDBRepository(ABC):
    @abstractmethod
    async def create_unique_question(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get_last_question(self, *args, **kwargs):
        pass

    @abstractmethod
    async def check_unique_dto(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_unique_dto(self, *args, **kwargs):
        pass
