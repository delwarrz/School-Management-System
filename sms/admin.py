from django.contrib import admin
from .models import Student, Course, Enrollment

# Register your models here.

# Showing Course CRUD in Admin Panel
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'created_at')

admin.site.register(Course, CourseAdmin)


# Showing Student CRUD in Admin Panel
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')

admin.site.register(Student, StudentAdmin)

# Showing Enrollment CRUD in Admin Panel
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_student_info', 'get_course_info', 'created_at')


    def get_student_info(self, obj):
        return "Name: " + obj.student.name + ", Email: " + obj.student.email + ", Phone: " + obj.student.phone
    
    get_student_info.short_description = 'Student Info'


    def get_course_info(self, obj):
        return "Name: " + obj.course.name + ", Code: " + obj.course.code
    
    get_course_info.short_description = 'Course Info'



admin.site.register(Enrollment, EnrollmentAdmin)