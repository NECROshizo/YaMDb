from django.db import models


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
        verbose_name_plural="Categories"

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
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Краткое описание',
    )
    #genre = models.ManyToManyField(
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Жанр',
        # додумать реализацию
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория',
    )


    def __str__(self):
        return self.name
