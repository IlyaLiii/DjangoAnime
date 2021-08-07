# Generated by Django 3.2.6 on 2021-08-07 09:29

import django.contrib.postgres.fields
import django.contrib.postgres.fields.citext
from django.contrib.postgres.operations import CITextExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        CITextExtension(),
        migrations.CreateModel(
            name='Anime_title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', django.contrib.postgres.fields.citext.CICharField(max_length=250, verbose_name='Имя на русском')),
                ('name_eng', django.contrib.postgres.fields.citext.CICharField(max_length=250, verbose_name='Имя на английском')),
                ('rating', django.contrib.postgres.fields.citext.CICharField(max_length=50, null=True, verbose_name='Рейтинг')),
                ('genre', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250, null=True), size=None, verbose_name='Жанры')),
                ('status', django.contrib.postgres.fields.citext.CICharField(choices=[('Announcement', 'Анонсировано'), ('Ongoing', 'Выходит'), ('Released', 'Вышло')], max_length=50, verbose_name='Статус')),
                ('release_date', django.contrib.postgres.fields.citext.CICharField(max_length=50, null=True, verbose_name='Дата выхода')),
                ('num_of_episodes', django.contrib.postgres.fields.citext.CICharField(max_length=50, null=True, verbose_name='Кол-во эпизодов')),
                ('pub_date', models.DateTimeField(null=True, verbose_name='date published')),
                ('extent', models.SmallIntegerField(choices=[(1, 'Отвратительно'), (2, 'Ужасно'), (3, 'Неприемлимо'), (4, 'Плохо'), (5, 'Средне'), (6, 'Пойдет'), (7, 'Хорошо'), (8, 'Отлично'), (9, 'Великолепно'), (10, 'АААА ДАА')], default=5)),
            ],
        ),
    ]