from django.shortcuts import render, redirect
from .forms import AttendanceForm
from .models import Student, Attendance
from django.utils import timezone
from django.contrib import messages
import qrcode
from io import BytesIO
from django.http import HttpResponse
import base64

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    return img_str

def class_qr_code(request):
    # Example data for QR code
    session_id = 1  # You should dynamically pass the session ID or other unique information
    qr_data = f"http://127.0.0.1:8000/attendance/mark/{session_id}"  # This could be any data you want to encode
    
    qr_image = generate_qr_code(qr_data)
    
    return render(request, 'attendance/class_qr_code.html', {'qr_image': qr_image})

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

