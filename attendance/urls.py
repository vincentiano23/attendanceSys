from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('view/', views.view_attendance, name='view_attendance'),
]
