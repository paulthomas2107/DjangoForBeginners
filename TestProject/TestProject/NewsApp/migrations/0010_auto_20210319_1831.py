# Generated by Django 3.1.7 on 2021-03-19 18:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0009_auto_20210319_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnotherPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 18, 31, 1, 92012, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='AnotherRestaurant',
            fields=[
                ('anotherplace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='NewsApp.anotherplace')),
                ('serves_pizza', models.BooleanField(default=False)),
                ('serves_tuna', models.BooleanField(default=False)),
            ],
            bases=('NewsApp.anotherplace',),
        ),
    ]