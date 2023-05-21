from app_service_1.uow.question_uow import QuestionUOW


async def recreate_exists_question(questions_int: int) -> None:
    """
    Функция вызывается фоновой задачей встроенного инструмента в FastApi.
    Рекурсивно вызывается пока не останутся только уникальные вопросы в БД.
    """
    if questions_int > 0:
        _, questions_int = await QuestionUOW(
            questions_int, retry=True
        ).get_and_create_question()
        await recreate_exists_question(questions_int)
