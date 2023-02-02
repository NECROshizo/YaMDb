from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User
from datetime import date


class Category(models.Model):
    """Категории произведений"""
    name = models.CharField(
        max_length=256,
        verbose_name='Категория',
    )
    slug = models.SlugField(
        unique=True,
        max_length=50
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Жанры произведений"""
    name = models.CharField(
        max_length=256,
        verbose_name='Жанр'
    )
    slug = models.SlugField(
        unique=True,
        max_length=50
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Произведения"""
    name = models.CharField(
        max_length=256,
        verbose_name='Произведение',
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        default=date.today().year,
        validators=[
            MinValueValidator(-3000),
            MaxValueValidator(date.today().year),
        ],
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Краткое описание',
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр',
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(models.Model):
    """Модель отзовов на произведение"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    score = models.IntegerField('Оценка', validators=[
        MaxValueValidator(limit_value=10, message='Оценка не более 10'),
        MinValueValidator(limit_value=1, message='Оценка не меньше 1'),
    ])
    text = models.TextField('Отзов')
    pud_data = models.DateTimeField(
        'Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return (
            f'Пользователь {self.author} '
            f'оценил на {self.score} '
            f'произведение "{self.title.name}".'
        )


class Comment(models.Model):
    """Модель коментариев к отзывам"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )

    reviews = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
    )
    text = models.TextField('Коментарий')
    pud_data = models.DateTimeField(
        'Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return (
            f'Пользователь {self.author} оставил коментарий'
            f'к отзыву {self.reviews.author.username}'
        )
