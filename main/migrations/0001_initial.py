# Generated by Django 4.0.4 on 2023-12-11 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.IntegerField(default=0, verbose_name='Количество уравнений')),
                ('a', models.TextField(verbose_name='Система уравнений')),
                ('x', models.TextField('Начальное приближение')),
                ('y', models.TextField(verbose_name='Решение системы уравнений')),
                ('iterations', models.IntegerField(default=0, verbose_name='Количество итераций')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания системы')),
            ],
            options={
                'verbose_name': 'Решение',
                'verbose_name_plural': 'Решения',
                'ordering': ['-create_date'],
            },
        ),
    ]
