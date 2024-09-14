from django.shortcuts import render, redirect
from .models import Student, Attendance
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
from django.utils import timezone
from django.contrib import messages
import matplotlib
matplotlib.use('Agg')



def mark_attendance(request):
    students = Student.objects.all()
    if request.method == 'POST':
        today = timezone.now().date()
        for student in students:
            status = request.POST.get(f'status_{student.id}', 'Absent')
            Attendance.objects.create(student=student,date=today, status=(status == 'Present'))
        return redirect('attendance:view_attendance')
    return render(request, 'attendance/mark_attendance.html', {'students': students})
   
def view_attendance(request):
    records = Attendance.objects.all().order_by('-date')
    return render(request, 'attendance/view_attendance.html', {'records': records})
  
 

def calculate_attendance_percentage(student):
    total_classes = Attendance.objects.filter(student=student).count()
    attended_classes = Attendance.objects.filter(student=student, status=True).count()
    if total_classes == 0:
        return 0
    return (attended_classes / total_classes) * 100

def attendance_statistics(request):
    students = Student.objects.all()
    attendance_data = []

    for student in students:
        percentage = calculate_attendance_percentage(student)
        attendance_data.append({'name': student.name, 'percentage': percentage})

  
    graph = generate_bar_graph(attendance_data)

    return render(request, 'attendance/attendance_statistics.html', {'attendance_data': attendance_data})

def generate_bar_graph(attendance_data):
    students = [student['name'] for student in attendance_data]
    attendance_percentages = [student['percentage'] for student in attendance_data]

    plt.figure(figsize=(2,1))
    plt.bar(students, attendance_percentages, color='blue')
    plt.xlabel('Students')
    plt.ylabel('Attendance Percentage')
    plt.title('Student Attendance Statistics')
    plt.xticks(rotation=45, ha='right')

    buffer = BytesIO()
    plt.savefig(buffer, format='png',bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    plt.close()

 
    return graph