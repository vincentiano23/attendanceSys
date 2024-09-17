from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('qr/', views.class_qr_code, name='class_qr_code'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('view/', views.view_attendance, name='view_attendance'),
    path('statistics/', views.attendance_statistics, name='attendance_statistics'),
   
    
]
