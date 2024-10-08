# Generated by Django 5.1.1 on 2024-09-16 13:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(default='course', max_length=100),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='registration_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
