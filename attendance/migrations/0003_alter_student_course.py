# Generated by Django 5.1.1 on 2024-09-13 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_student_course_alter_student_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(default='course', max_length=100),
        ),
    ]
