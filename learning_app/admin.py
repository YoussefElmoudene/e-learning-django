from django.contrib import admin

from learning_app.models import Student


# Register your models here.
@admin.register(Student)
class AuthorAdmin(admin.ModelAdmin):
    pass
