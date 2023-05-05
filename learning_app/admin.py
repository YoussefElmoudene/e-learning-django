from django.contrib import admin
from learning_app.models import Teacher, UserModel
from learning_app.models import Student, Teacher, Course, Inscription, Chapter


@admin.register(UserModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'password', 'name', 'phone', 'role')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'level')
    ordering = ('level',)
    list_filter = ('level',)
    search_fields = ('level',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'description', 'dateCreated', 'duration', 'price', 'oldPrice')
    ordering = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('date', 'course', 'student')
    ordering = ('date',)
    list_filter = ('date',)
    search_fields = ('date',)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'description', 'img', 'video')
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Teacher)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile', 'salaire', 'grade',
        'specialty')
