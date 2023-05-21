from abc import ABC, abstractmethod


class FileRepository(ABC):
    @abstractmethod
    def create_name_with_format(self, *args, **kwargs):
        pass

    @abstractmethod
    def convert_to_mp3(self, *args, **kwargs):
        pass

    @abstractmethod
    def validator_old_name(self, *args, **kwargs):
        pass

    @abstractmethod
    async def create_in_db(self, *args, **kwargs):
        pass

    @abstractmethod
    def download_file(self, *args, **kwargs):
        pass
