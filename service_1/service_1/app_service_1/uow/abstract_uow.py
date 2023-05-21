from abc import ABC


class AbstractUnitOfWork(ABC):
    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass
