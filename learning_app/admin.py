from django.contrib import admin

from learning_app.models import Teacher, UserModel


# Register your models here.

@admin.register(Teacher)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile', 'salaire', 'grade',
        'specialty')


@admin.register(UserModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'password', 'name', 'phone', 'role')
