from abc import ABC, abstractmethod


class AbstractUnitOfWork(ABC):
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    @abstractmethod
    async def create_and_save_mp3(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get(self, *args, **kwargs):
        pass
