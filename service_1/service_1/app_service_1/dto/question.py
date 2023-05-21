from datetime import datetime

from pydantic import BaseModel


class QuestionDTO(BaseModel):

    """Контейнер данных с валидацией для вопросов"""

    id: int
    answer: str
    question: str
    created_at: datetime
