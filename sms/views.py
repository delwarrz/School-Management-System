from django.shortcuts import render, redirect
from .models import Student, Course, Enrollment
from .forms import CourseForm, StudentForm, EnrollmentForm
from django.contrib import messages

# Create your views here.

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully')
            return redirect('courses')
    else:
        form = CourseForm()

    courses = Course.objects.all()    
    return render(request, 'courses.html', {'courses': courses, 'form': form})

def add_student(request):
    if request.method == 'POST':
       form = StudentForm(request.POST)
       if form.is_valid():
           form.save()
           
           messages.success(request, 'Student added successfully')
           return redirect('home')
    else:
        form = StudentForm()
    courses = Course.objects.all()
    return render(request, 'add_student.html', {'courses': courses, 'form': form})

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully')
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    courses = Course.objects.all()
    return render(request, 'edit_student.html', {'courses': courses, 'form': form})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, 'Student deleted successfully')
    return redirect('home')

def enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            course = form.cleaned_data['course']
            if Enrollment.objects.filter(student=student, course=course).exists():
                messages.warning(request, 'This student is already enrolled in this course')
            else:
                form.save()
                messages.success(request, 'Enrollment added successfully')
            return redirect('enrollment')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment.html', {'form': form})

def student_details(request, id):
    student = Student.objects.get(id=id)
    enrollments = Enrollment.objects.filter(student=student)
    return render(request, 'student_details.html', {'student': student, 'enrollments': enrollments})

