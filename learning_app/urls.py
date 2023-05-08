from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', include('courses.urls')),
    path('teacher-dashboard', views.show_teacher, name="teacher"),
    path('teacher-courses', views.show_teacher_courses, name="teacher-courses"),
    path('teacher-course-chapters', views.show_course_chapters, name="teacher-course-chapters"),
    path('teacher-create-course', views.show_teacher_create_course, name="teacher-create-course"),
    path('teacher-create-chapter', views.show_teacher_create_chapter, name="teacher-create-chapter"),
    path('new-student', views.studentForm, name="student-form"),
    path('course/<int:id>', views.show_course_details, name='course_detail'),
    path('login', views.show_login_page, name="login"),
    path('doLogin', views.do_login, name="do_login"),
    path('logout', views.logout_view, name="logout"),
    path('create_course', views.create_course, name="create_course"),
    path('create_chapter', views.create_chapter, name="create_chapter"),
    path('create_student', views.create_student, name="create-student"),
]
