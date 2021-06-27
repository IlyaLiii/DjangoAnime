# Generated by Django 3.2.3 on 2021-05-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_name_jp_anime_title_name_eng'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime_title',
            name='rating',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='anime_title',
            name='status',
            field=models.CharField(choices=[('Announcement', 'Анонсировано'), ('Ongoing', 'Сейчас выходит'), ('Released', 'Вышедшее')], max_length=50),
        ),
    ]
