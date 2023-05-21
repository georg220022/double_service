#### Оба сервиса собираются из 1 Dockerfile, и поднимаются по 1-й команде. Скриншоты примеров сделаны в Postman.

#### Стек: FastApi, Alembic, SQLAlchemy, Docker, Python3, Pydantic
  
#### Запуск:
- перейти в папку с проектом (где лежит docker-compose.yml)
- выполнить docker-compose up
- дождаться запуска контейнеров (будут запущены оба сервиса)

## Сервис 1 - Получение вопросов по API
- Не более 100 вопросов за 1 раз  
   
Отправить POST запрос на адрес http://localhost:8000/api/v1/save_new_question  
Тело запроса:  
{  
    "questions_num": int  
}   
Пример:  
![Получить вопросы](https://github.com/georg220022/spring_2023/blob/main/%D0%92%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B.png)  
  
Креды для подключения извне к БД:  
адрес: localhost:5433   
PASSWORD и USER и DB = "gera"  
  
## Сервис 2 - Конвертация файлов  
- Отправка файла на конвертацию требует api ключ, остальные эндпоинты без ключа  
- Файл должен быть в формате .wav  
  
Регистрация: отправить POST запрос  
http://localhost:8001/api/v1/registration  
  
Тело запроса:  
{  
    "username": "Ivan"  
}  
![Регистрация](https://github.com/georg220022/spring_2023/blob/main/%D0%A0%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F.png)  
  
Перед отправкой файла на конвертацию добавим API ключ.  
1) Перейти во вкладку Authorization  
2) Выбрать тип API KEY  
3) ключ указать "api_key"  
4) в значение добавить ключ полученный при регистрации  
5) выбрать параметр Header  
![Добавление API ключа](https://github.com/georg220022/spring_2023/blob/main/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BA%D0%BB%D1%8E%D1%87%D0%B0.png)  
   
Отправка файла на конвертацию: отправить POST запрос  
http://localhost:8001/api/v1/upload_wav  
Тело должно содержать файл и user_id
1) Перейти во вкладку Body
2) У ключа "file" выбрать в выпадающем списке тип File, в значение добавить сам .wav файл
3) "user_id" это id пользователя полученный при регистрации
![Добавление API ключа](https://github.com/georg220022/spring_2023/blob/main/%D0%9A%D0%BE%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%B0%D1%86%D0%B8%D1%8F.png)  

Скачивание файла: отправить GET запрос
Полученный в ответ url при отправке файла на конвертацию можно просто вставить в адресную строку браузера
"http://127.0.0.1:8001/download/d7fa38a8-dc24-4b23-ad5f-b6741274e8f9.mp3"

Вроде все :)
![Jokes Card](https://readme-jokes.vercel.app/api)
