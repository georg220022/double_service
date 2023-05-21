Оба сервиса собираются из 1 Dockerfile, и поднимаются по 1-й команде. Скриншоты примеров сделаны в Postman.

Стек: FastApi, Alembic, SQLAlchemy, Docker, Python3, Pydantic

Запуск:
- перейти в папку с проектом (где лежит docker-compose.yml)
- выполнить docker-compose up
- дождаться запуска контейнеров (будут запущены оба сервиса)

Сервис 1 - Получение вопросов по API
- Не более 100 вопросов за 1 раз  
 
Отправить POST запрос на адрес http://localhost:8000/api/v1/save_new_question  
Тело запроса:  
{  
    "questions_num": int  
}  
![Получить вопросы]([https://github.com/jon/coolproject/raw/master/image/image.png](https://github.com/georg220022/spring_2023/blob/main/%D0%92%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B.png))

Креды для подключения извне к БД:  
адрес: localhost:5433  
PASSWORD/USER/DB = "gera"

Сервис 2 - Конвертация файлов
- Отправка файла на конвертацию требует api ключ, остальные эндпоинты без ключа
- Файл должен быть в формате .wav

Регистрация: отправить POST запрос
http://localhost:8001/api/v1/registration  

Тело запроса:
{
    "username": "Ivan"
}

Отправка файла на конвертацию: отправить POST запрос
http://localhost:8001/api/v1/upload_wav
