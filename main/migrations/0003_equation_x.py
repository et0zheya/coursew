# Generated by Django 4.1.2 on 2023-12-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_equation_iterations'),
    ]

    operations = [
        migrations.AddField(
            model_name='equation',
            name='x',
            field=models.TextField(default=0, verbose_name='Начальное приближение'),
            preserve_default=False,
        ),
    ]
