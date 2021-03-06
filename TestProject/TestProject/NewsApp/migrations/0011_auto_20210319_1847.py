# Generated by Django 3.1.7 on 2021-03-19 18:47

import datetime
import django.contrib.auth.models
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('NewsApp', '0010_auto_20210319_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
            ],
            options={
                'ordering': ('username',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 18, 47, 4, 746653, tzinfo=utc)),
        ),
    ]
