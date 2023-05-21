from settings.settings import DOWNLOAD_PATH, MAX_LEN_FILE_NAME, MIN_LEN_FILE_NAME


class ServerMessages:
    NOT_VALID_USER = {"detail": "Не верный API ключ или id пользователя"}
    CREATED_FILE = DOWNLOAD_PATH
    ERROR_FILENAME = {"detail": "Песня должна быть в формате .wav"}
    ERROR_LENGTH_FILE_NAME = {
        "detail": f"количество символов в названии не менее {MIN_LEN_FILE_NAME} символов и не более {MAX_LEN_FILE_NAME}"
    }
    ERROR_SAVE_FILE_DB = {"detal": "Не удалось сохранить файл в БД"}
    DOWNLOAD_LINK = {"detail": DOWNLOAD_PATH}
    NOT_FOUND_FILE = {"detail": "Не найден файл для скачивания"}
    ERROR_CONVERT = {"detail": "Не удалось конвертировать файл"}
    NOT_FOUND_USER = {"detail": "Не удалось найти пользователя"}
