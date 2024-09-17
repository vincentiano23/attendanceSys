from django.utils import timezone
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100, default='course')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

   

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.name} - {self.date}'


