from app_service_1.dto.question import QuestionDTO
from app_service_1.models import question_
from settings.settings import db_async
from sqlalchemy import desc, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from service_1.app_service_1.repositories.db.abstract_db_repository import (
    AbstractDBRepository,
)


class CrudQuestion(AbstractDBRepository):
    """CRUD для вопросов"""

    async def create_unique_question(
        self, dto_list: list[QuestionDTO], retry: bool = False
    ) -> tuple[QuestionDTO | None | list, int]:
        """
        Функция создает уникальные вопросы в БД, возвращает 2 параметра:
        1) последний созданный вопрос до сохранения нового вопроса или пустой список если БД пуста.
        2) количество не уникальных вопросов
        """
        async with db_async as db:
            exists_id_list = await self.check_unique_dto(db, dto_list)
            unique_question_dto_list = self.get_unique_dto(dto_list, exists_id_list)
            last_question = None
            if not retry:
                last_question = await self.get_last_question(db)
            if unique_question_dto_list:
                query_create_question = insert(question_).values(
                    unique_question_dto_list
                )
                await db.execute(query_create_question)
                await db.commit()
                return last_question, len(exists_id_list)
            return last_question, len(dto_list)

    async def get_last_question(self, db: AsyncSession) -> list | QuestionDTO:
        """
        Функция возвращает последний созданный вопрос из БД, если БД пустая то вернется пустой список
        """
        last_question_query = (
            select(question_.c["id", "answer", "created_at", "question"])
            .order_by(desc(question_.c.date_add))
            .limit(1)
        )
        if last_question := (await db.execute(last_question_query)).fetchall():
            last_question = last_question[0]
            return QuestionDTO(
                id=last_question[0],
                answer=last_question[1],
                created_at=last_question[2],
                question=last_question[3],
            )
        return []

    async def check_unique_dto(
        self, db: AsyncSession, dto_list: list[QuestionDTO]
    ) -> list[int]:
        """
        Функция возвращает список уже существующих id вопросов в БД
        """
        query_exists_id = select(question_.c.id).where(
            question_.c.id.in_([dto.id for dto in dto_list])
        )
        return [id_[0] for id_ in await db.execute(query_exists_id)]

    def get_unique_dto(self, dto_list, exists_id_list) -> list[dict]:
        """
        Функция возвращает список уникальных вопросов для сохранения в БД
        """
        return [
            dto_object.__dict__
            for dto_object in dto_list
            if dto_object.id not in exists_id_list
        ]
