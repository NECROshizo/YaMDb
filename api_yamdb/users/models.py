from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        verbose_name='Адрес электронной почты'
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Фамилия'
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время регистрации'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Дополнительная информация'
    )
