from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('add_student', views.add_student, name='add_student'),
    path('student_details/<int:id>/', views.student_details, name='student_details'),
    path('edit_student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    path('enrollment', views.enrollment, name='enrollment'),
]
