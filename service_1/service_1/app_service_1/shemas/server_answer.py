class MessageResponse:
    """
    Константы для ответа сервера.
    Ключ для текста в словаре должен быть только 'detail'.
    """

    BAD_RESPONSE_JSERVICE = {"detail": "Jservice отдал неожиданный ответ"}
