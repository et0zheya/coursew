# Generated by Django 4.0.4 on 2023-12-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equation',
            name='iterations',
            field=models.IntegerField(default=0, verbose_name='Количество итераций'),
        ),
    ]