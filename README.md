# YaTube

### Описание проекта:

api_final_yatube является API-интерфейсом проекта YATUBE, к которому могут обращаться другие приложения для взаимодействия с YATUBE.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Elijah-iSO/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры работы API:

### POSTS:

1) Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.
эндпоинт:
```
GET-> /api/v1/posts/
```
ответ:
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

2) Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
```
POST-> /api/v1/posts/
```
3) Получение публикации по id.
```
GET-> /api/v1/posts/{id}/
```
4) Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
```
PUT-> /api/v1/posts/{id}/
```
6) Частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
```
PATCH-> /api/v1/posts/{id}/
```
примеры запросов в работе с posts:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
примеры ответов в работе с posts:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```   
7) Удаление публикации по id. Удалить публикацию может только автор публикации. Анонимные запросы запрещены.
```
DELETE-> /api/v1/posts/{id}/
```

### COMMENTS:

1) Получение всех комментариев к публикации.
```
GET-> /api/v1/posts/{post_id}/comments/
```
2) Добавление нового комментария к публикации. Анонимные запросы запрещены.
```
POST-> /api/v1/posts/{post_id}/comments/
```
3) Получение комментария к публикации по id.
```
GET-> /api/v1/posts/{post_id}/comments/{id}/
```
4) Обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
```
PUT-> /api/v1/posts/{post_id}/comments/{id}/
```
5) Частичное обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
```
PATCH-> /api/v1/posts/{post_id}/comments/{id}/
```

примеры запросов в работе с comments:
```
{
  "text": "string"
}
```
примеры ответов в работе с comments:
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
6) Удаление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
```
DELETE-> /api/v1/posts/{post_id}/comments/{id}/
```

### GROUP:

1) Получение списка доступных сообществ.
```
GET-> /api/v1/groups/
```
2)Получение информации о сообществе по id.
```
GET-> /api/v1/groups/{id}/
```
примеры ответов в работе с groups:
```
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```

### FOLLOW:

1) Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены. Возможен поиск по подпискам по параметру search.
```
GET-> /api/v1/follow/
```
2) Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
```
POST-> /api/v1/follow/
```
примеры запросов в работе с follow:
```
{
  "following": "string"
}
```
примеры ответов в работе с follow:
```
{
  "user": "string",
  "following": "string"
}
```

### JWT:

1) Получение JWT-токена.
```
POST-> /api/v1/jwt/create/
```
2) Обновление JWT-токена.
```
POST-> /api/v1/jwt/refresh/
```
3) Проверка JWT-токена.
```
POST-> /api/v1/jwt/verify/
```
