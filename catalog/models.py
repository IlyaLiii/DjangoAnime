from django.contrib.auth.models import User
from django.db import models

from django.db.models import ManyToManyField


class Genres(models.Model):
    genre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return '/catalog/genre_search/%s/' % self.pk


# Create your models here.
class Anime_title(models.Model):
    Status_of_title = (
        ('Announcement', 'Анонсировано'),
        ('Ongoing', 'Выходит'),
        ('Released', 'Вышло'),
    )

    class Quality_grade(models.IntegerChoices):
        disgusting = 1, 'Отвратительно'
        awful = 2, 'Ужасно'
        unacceptably = 3, 'Неприемлимо'
        bad = 4, 'Плохо'
        plus_minus = 5, 'Средне'
        fine = 6, 'Пойдет'
        good = 7, 'Хорошо'
        excellent = 8, 'Отлично'
        toppingly = 9, 'Великолепно'
        naruto = 10, 'Иди нахуй с такими оценками'

    name_ru = models.CharField(max_length=250, verbose_name='Имя на русском')
    name_eng = models.CharField(max_length=250, verbose_name='Имя на английском')
    rating = models.CharField(max_length=50, null=True, verbose_name='Рейтинг')
    # genre = models.CharField(max_length=250, null=True, verbose_name='Жанры')
    status = models.CharField(max_length=50, choices=Status_of_title, verbose_name='Статус')
    release_date = models.CharField(max_length=50, null=True, verbose_name='Дата выхода')
    num_of_episodes = models.CharField(max_length=50, null=True, verbose_name='Кол-во эпизодов')
    pub_date = models.DateTimeField('date published', null=True)
    extent = models.SmallIntegerField(choices=Quality_grade.choices, default=Quality_grade.plus_minus)
    genre = ManyToManyField(Genres)

    class Meta:
        verbose_name_plural = 'Тайтлы'
        verbose_name = 'Тайтл'
        get_latest_by = 'pub_date'
        # %(class)s - имя класса модели
        indexes = [
            models.Index(fields=['rating', 'status', 'release_date'],
                         name='%(class)s_main'),
            models.Index(fields=['name_ru', 'rating', 'num_of_episodes'],
                         name='%(class)s_second'),
        ]

    def __str__(self):
        return self.name_ru

    def get_absolute_url(self):
        return '/catalog/%s/' % self.pk

    def name_and_rating(self):
        if self.name_ru and self.rating:
            return '%s %s' % (self.name_ru, self.rating)

