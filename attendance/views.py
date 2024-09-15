from django.shortcuts import render, redirect
from .models import Student, Attendance
from django.utils import timezone
from django.contrib import messages


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

  

    return render(request, 'attendance/attendance_statistics.html', {'attendance_data': attendance_data})

