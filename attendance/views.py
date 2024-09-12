from django.shortcuts import render, redirect
from .models import Student, Attendance
from django.utils import timezone

def mark_attendance(request):
    students = Student.objects.all()
    if request.method == 'POST':
        for student in students:
            status = request.POST.get(f'status_{student.id}', 'Absent')
            Attendance.objects.create(student=student, status=status)
        return redirect('attendance:view_attendance')
    return render(request, 'attendance/mark_attendance.html', {'students': students})

def view_attendance(request):
    records = Attendance.objects.all().order_by('-date')
    return render(request, 'attendance/view_attendance.html', {'records': records})

