from django.contrib import admin
from learning_app.models import Teacher, UserModel
from learning_app.models import User, Student, Teacher, Course, Inscription, Chapter


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('name', 'phone', 'email', 'password', 'role')
    ordering=('name',)
    list_filter=('name', 'email')
    search_fields=('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('level',)
    ordering=('level',)
    list_filter=('level',)
    search_fields=('level',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('salaire', 'grade', 'specialty')
    ordering=('salaire',)
    list_filter=('grade',)
    search_fields=('specialty',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('title', 'level', 'description', 'dateCreated', 'duration', 'price')
    ordering=('level',)
    list_filter=('level',)
    search_fields=('title',)

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display=('date',)
    ordering=('date',)
    list_filter=('date',)
    search_fields=('date',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'img', 'video')
    ordering=('name',)
    list_filter=('name',)
    search_fields=('name',)


@admin.register(Teacher)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile', 'salaire', 'grade',
        'specialty')


@admin.register(UserModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'password', 'name', 'phone', 'role')

admin.site.register(User, UserAdmin)
