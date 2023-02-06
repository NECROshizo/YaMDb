﻿import csv

from django.core.management import BaseCommand
from django.db.models import ForeignKey
from django.apps import apps

from reviews.models import (
    User, Title, GenreTitle, Category, Genre, Review, Comment
)

FILES_MODELS = [
    ['users.csv', User],
    ['category.csv', Category],
    ['genre.csv', Genre],
    ['titles.csv', Title],
    ['genre_title.csv', GenreTitle],
    ['review.csv', Review],
    ['comments.csv', Comment]
]


class Command(BaseCommand):
    help = 'Загрузка данных из static/data в базу данных'

    def handle(self, *args, **kwargs):
        for file, model in FILES_MODELS:
            with open('static/data/' + file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    record = {}
                    for key, value in row.items():
                        model_field = model._meta.get_field(key)
                        if (isinstance(model_field, ForeignKey)
                            and '_id' not in key):
                            key = f'{key}_id'
                            record[key] = value
                        else:
                            record[key] = value
                        model.objects.get_or_create(**row)
                        print(key)
        self.stdout.write(self.style.SUCCESS('Новые данные внесены в базу'))
