# Practice Task

Простой поисковик по текстам документов с использованием FastAPI. 
Данные хранятся в PostgreSql, поисковый индекс в Elasticsearch.
Тестовые данные брались из ./posts.csv. 

__Структура БД:__

- `id` - уникальный для каждого документа;
- `rubrics` - массив рубрик;
- `text` - текст документа;
- `created_date` - дата создания документа.


__Структура Индекса:__

- `iD` - id из базы;
- `text` - текст из структуры БД.


__Методы:__

- Сервис принимает на вход произвольный текстовый запрос, ищет по тексту документа в индексе и возвращает первые 20 документов;
- Удаление документа из БД и индекса по полю  `id`.


__Гайд по поднятию:__
(доработать: внести команды в docker-compose
 - подгружение данных в постгрес
psql -d postgres
 - забираем из csv
COPY page(text, date_creation, rubrics)
FROM './posts.csv'
DELIMITER ','
CSV HEADER;
 - миграции
alembic upgrade head
)

 # docker build -t searcher ./
 # docker-compose up -d

(тоже внести в docker-compose - пофиксить порт - localhost:8000 только в докере)
 - uvicorn backend.main:app --reload

Смотрим http://localhost:8000/docs.

