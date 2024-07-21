# Тестовое задание на python-разработчика для проекта guider.pro

## Как запустить проект

### 1. Загрузить проект и развернуть виртуальное окружение

1.1. Введите команду в терминал

```
git clone git@github.com:OlegPrizov/guider_test.git
```

1.2. Перейдите в проект

```
cd guider_test/
```

1.3. Установите и активируйте виртуальное окружение

```
python -m venv venv
source venv/bin/activate
```

### 2. Установить зависимости и загрузить тестовые данные

2.1. Установите нужные библиотеки

```
pip install -r requirements.txt
```

2.2. Установите зависимости

```
python manage.py makemigrations
python manage.py migrate
```

2.3. Загрузите тестовые данные

```
python manage.py data_loader
```

Тестовые данные включают в себя:
1. Город: Москва
2. Улицы: Никольская и Мясницкая
3. Магазины: по 3 магазина на каждой улице с разным временем работы

### 3. Запустите проект

3.1. Введите команду

```
python manage.py runserver
```

### 3. Проверьте работоспособность проекта

Для этого можно использовать [Postman](https://www.postman.com/downloads/)

- GET .../city/ — получение списка всех городов из базы данных;

Пример: http://127.0.0.1:8000/city/

```JSON
[
    {
        "id": 1,
        "name": "Moscow"
    }
]
```

- GET .../city/{city_id}/street/ — получение списка всех улиц указанного города.

Пример: http://127.0.0.1:8000/city/1/street/

```JSON
[
    {
        "id": 1,
        "city": {
            "id": 1,
            "name": "Moscow"
        },
        "name": "Мясницкая"
    },
    {
        "id": 2,
        "city": {
            "id": 1,
            "name": "Moscow"
        },
        "name": "Никольская"
    }
]
```

- POST .../shop/ — создание нового магазина. Пример можете найти ниже.

Пример: http://127.0.0.1:8000/shop/

```JSON
{
    "name": "Тестовый магазин",
    "city": "Санкт-Петербург",
    "street": "Ленина",
    "house_number": 10,
    "opening_time": "9:00",
    "closing_time": "21:15"
}
```
- GET .../shop/?street=&city=&open=0/1 - получение списка магазинов. (Фильтры необязательны)

Пример: http://127.0.0.1:8000/shop/?street=Никольская&city=Moscow&open=1

```JSON
[
    {
        "id": 6,
        "name": "Азбука вкуса",
        "city": "Moscow",
        "street": "Никольская",
        "house_number": 7,
        "opening_time": "01:00:00",
        "closing_time": "10:00:00"
    }
]
```