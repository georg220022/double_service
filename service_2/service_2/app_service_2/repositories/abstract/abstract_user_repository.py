from abc import ABC, abstractmethod


class AbstractUserRepository(ABC):
    @abstractmethod
    async def create(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get(self, *args, **kwargs):
        pass

    @abstractmethod
    async def delete(self, *args, **kwargs):
        pass
