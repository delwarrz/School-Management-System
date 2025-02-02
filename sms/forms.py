from django import forms
from .models import Course, Student, Enrollment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded py-2 px-3 text-gray-700'}),
            'code': forms.TextInput(attrs={'class': 'border rounded py-2 px-3 text-gray-700'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded py-2 px-3 text-gray-700'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded py-2 px-3 text-gray-700', 'type': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'border rounded py-2 px-3 text-gray-700'}),
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
        widgets = {
            'student': forms.Select(attrs={'class': 'border rounded py-2 px-3 text-gray-700'}),
            'course': forms.Select(attrs={'class': 'border rounded py-2 px-3 text-gray-700'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.all()
        self.fields['student'].label_from_instance = lambda obj: f"{obj.name} ({obj.email})"
        self.fields['course'].queryset = Course.objects.all()
        self.fields['course'].label_from_instance = lambda obj: f"{obj.name} ({obj.code})"