from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', include('courses.urls')),
    path('teacher-dashboard', views.show_teacher, name="teacher"),
    path('teacher-courses', views.show_teacher_courses, name="teacher-courses"),
    path('teacher-create-course', views.show_teacher_create_course, name="teacher-create-course"),
    path('login', views.show_login_page, name="login"),
    path('doLogin', views.do_login, name="do_login"),
    path('logout', views.logout_view, name="logout"),
    path('create_course', views.create_course, name="create_course"),
    path('create-student', views.create_student, name="create-student"),
]
