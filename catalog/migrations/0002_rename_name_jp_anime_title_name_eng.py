# Generated by Django 3.2.3 on 2021-05-28 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime_title',
            old_name='name_jp',
            new_name='name_eng',
        ),
    ]
