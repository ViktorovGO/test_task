# Web-приложение для сбора информации о валютах.

## Установка и запуск

 Для MacOs и Linux вместо python использовать python3

## **1. Клонировать репозиторий:**
```
git clone https://github.com/ViktorovGO/test_task.git
```

## **2. Перейти в папку проекта:**
```
cd test_task/
```

## **3. Cоздать и активировать виртуальное окружение:**
```
python -m venv venv
```

Для Windows:
```
venv\Scripts\activate.bat
```

Для MacOs/Linux:
```
source venv/bin/activate
```

## **4. Установить зависимости из файла requirements.txt:**
- Обновить пакетный менеджер pip
```
python -m pip install --upgrade pip
```

- Установить зависимости
```
pip install -r requirements.txt
```

## **5. Запустить веб сервер**
~~~
cd backend/
~~~
- Создать миграции
```
python manage.py makemigrations
```
- Применить миграции
```
python manage.py migrate
```

- Обновить данные о валюте
~~~
python manage.py get_currency
~~~
- Запустить сервер
~~~
python manage.py runserver
~~~
- Курсы валют доступны по урлу
~~~
http://127.0.0.1:8000/show_rates/?date=2024-05-15
~~~
