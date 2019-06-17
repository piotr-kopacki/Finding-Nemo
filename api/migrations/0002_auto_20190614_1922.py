# Generated by Django 2.2.2 on 2019-06-14 17:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='score',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(0.5)]),
        ),
    ]