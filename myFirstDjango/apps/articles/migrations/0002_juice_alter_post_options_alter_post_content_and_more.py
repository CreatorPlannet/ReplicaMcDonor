# Generated by Django 4.1.3 on 2022-11-24 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title2', models.CharField(max_length=255, verbose_name='Название Сока')),
                ('content2', models.TextField(verbose_name='Доп. ингридиенты')),
                ('postDate2', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата добавления нового сока')),
                ('source2', models.CharField(max_length=50, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Сок',
                'verbose_name_plural': 'Соки',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Бургер', 'verbose_name_plural': 'Бургеры'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Доп. ингридиенты'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postDate',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата добавления нового бургера'),
        ),
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.CharField(max_length=50, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название Бургера'),
        ),
    ]
