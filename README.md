# Проект api_yamdb
Проект для обучения.

![](https://img.shields.io/badge/python-3.9.8-blue)
![](https://img.shields.io/badge/Django-3.2-blue)
![](https://img.shields.io/badge/DjangoRest-3.12.4-blue)
![](https://img.shields.io/badge/DjangoRestSimpleJWTt-4.7.2-blue)

## Как запустить
1.Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/NECROshizo/api_yamdb.git
```

2 Перейти

```
cd api_yamdb
```

3 Cоздать виртуальное окружение:

```
py -m venv venv
```

4 Активировать виртуальное окружение:

```
source venv/bin/activate
```

5 Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

6 Выполнить миграции:

```
py manage.py migrate
```

7 Запустить проект:

```
py manage.py runserver
```