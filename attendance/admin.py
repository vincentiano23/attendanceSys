from django.contrib import admin

from .models import Department, Student, Attendance

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Attendance)

