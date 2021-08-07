from django.db import models
from django.contrib.postgres.fields import ArrayField, CICharField


class PGSRubric(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    tags = ArrayField(base_field=models.CharField(
        max_length=20
    ))


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
        naruto = 10, 'АААА ДАА'

    name_ru = CICharField(max_length=250, verbose_name='Имя на русском')
    name_eng = CICharField(max_length=250, verbose_name='Имя на английском')
    rating = CICharField(max_length=50, null=True, verbose_name='Рейтинг')
    genre = ArrayField(base_field=models.CharField(max_length=250, null=True), verbose_name='Жанры')
    status = CICharField(max_length=50, choices=Status_of_title, verbose_name='Статус')
    release_date = CICharField(max_length=50, null=True, verbose_name='Дата выхода')
    num_of_episodes = CICharField(max_length=50, null=True, verbose_name='Кол-во эпизодов')
    pub_date = models.DateTimeField('date published', null=True)
    extent = models.SmallIntegerField(choices=Quality_grade.choices, default=Quality_grade.plus_minus)

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



    # def get_absolute_url(self):
    #     return '/catalog/genre_search/%s/' % self.pk
