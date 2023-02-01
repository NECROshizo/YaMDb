from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class UserRoles(models.TextChoices):
        USER = 'user', ('User')
        MODERATOR = 'moderator', ('Moderator')
        ADMIN = 'admin', ('Admin')

    username = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
        verbose_name='Адрес электронной почты'
    )
    first_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
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
    role = models.CharField(
        max_length=100,
        choices=UserRoles.choices,
        default=UserRoles.USER,
        verbose_name='Пользовательская роль (определяет права доступа)'
    )
