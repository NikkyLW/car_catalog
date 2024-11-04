Тестовое задание для Python (Django) Backend - разработчика

Суть задания: Сделать каталог автомобилей, просмотром карточек автомобилей и оставление/вывод комментриев к продуктам (автомобилям). На сайте реализована CRUD функционльность, а также API

Проект состоит из несколькох Application

1.Car (Автомобили)
2.Comment (Комментарии)
3.Main (Главная)
4.Api (RestAPI)
-----------------------------------------------------
Инструкция по запуску проекта на локальной машине
1. Склонируйте репозиторий к себе на ПК
- git clone https://github.com/NikkyLW/car_catalog.git
2. Создайте и запустите виртуальное окружение для проекта
- python -m venv venv
- venv\Scripts\activate (через CMD, а не PowerShell)
3. Установите нужные пакеты, которые прописаны в requirements.txt
- pip install -r requirements.txt
4. Отредактируйте конфиги в файле app/setting.py
  4.1 Postgresql
`
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ИМЯ БАЗЫ ДАННЫХ',
        'USER': 'ПОЛЬЗОВАТЕЛЬ',
        'PASSWORD': 'ПАРОЛЬ',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
`
5. Запустите проект на локальном сервере
- python manage.py runserver
6. `127.0.0.1:8000` - Тестируйте 

-----------------------------------------------------
Документация API:

Все тесты лучше проводить с программой PostMan
Удобно и практично, ниже описаны эндпоинты для тестов

Получение всех автомобилей:
Эндпоинт - `GET /api/cars/`
Вывод:
`
[
  {
      "id": int,
      "make": str,
      "model": str,
      "year": str,
      "description": str,
      "created_at": str,
      "updated_at": str,
      "owner": int
  }
]
`

Получение определенного автомобиля:
Эндпоинт - `GET /api/cars/<id>/`
Вывод:
`
  {
      "id": int,
      "make": str,
      "model": str,
      "year": str,
      "description": str,
      "created_at": str,
      "updated_at": str,
      "owner": int
  }
`

Добавление нового автомобиля:
Эндпоинт - `POST /api/car/create/`
Тело запроса:
`
{
    "make": str,
    "model": str,
    "year": str,
    "description": str,
    "owner": str
}
`
Вывод:
`
{
    "status": str,
    "id": int
}
`

Обновление данных об автомобиле:
Эндпоинт - `PUT /api/cars/<id>/`
Тело запроса:
`
{
    "make": str,
    "model": str,
    "year": str,
    "description": str,
    "owner": str
}
`
Вывод:
`
{
    "status": str,
    "id": int
}
`

Удаление автомобиля с сайта:
Эндпоинт - `DELETE /api/cars/<id>/`
Вывод:
`
{
    "status": str,
}
`

Получение комментариев у определенного автомобиля автомобилей:
Эндпоинт - `GET /api/cars/<id>/comments/`
Вывод:
`
[
    {
        "id": int,
        "content": str,
        "created_at": str,
        "car": int,
        "author": int
    }
]
`

Создание комментария к определенному автомобилю:
Эндпоинт - `POST /api/cars/<id>/comments/`
Тело запроса:
`
{
    "content": str,
    "author": str
}
`
Вывод:
`
{
    "status": str,
    "id": int,
    "user_id": int,
    "car_id": int
}
`
