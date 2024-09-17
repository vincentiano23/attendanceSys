from django import forms

class AttendanceForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)