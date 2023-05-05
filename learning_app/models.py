import datetime
from enum import Enum

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils import timezone


class Role(Enum):
    STUDENT = 'STUDENT'
    TEACHER = 'TEACHER'
    ADMIN = 'ADMIN'


class UserModel(User):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.email + ' , ' + self.role + ' , ' + self.password

    class Meta:
        base_manager_name = 'objects'


class Student(models.Model):
    user_profile = models.OneToOneField(UserModel, on_delete=models.CASCADE, null=True, default=None)
    level = models.CharField(max_length=20)


class Teacher(models.Model):
    user_profile = models.OneToOneField(UserModel, on_delete=models.CASCADE, null=True, default=None)
    salaire = models.FloatField()
    grade = models.CharField(max_length=20)
    specialty = models.CharField(max_length=255)


class Course(models.Model):
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    description = models.TextField()
    dateCreated = models.DateField()
    duration = models.CharField(max_length=20)
    price = models.FloatField()
    oldPrice = models.FloatField(default=None, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' , ' + self.level + ' , ' + self.description \
            + ' , ' + self.dateCreated.__str__() + ' , ' + self.duration \
            + ' , ' + self.teacher.user_profile.role.__str__() + ' , ' + self.teacher.user_profile.name \
            + ' , ' + self.teacher.user_profile.email.__str__() + ' , ' + self.teacher.user_profile.phone \
            + ' , ' + self.price.__str__() + ' , ' + self.oldPrice.__str__()


class Inscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()


class Chapter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='chapter_images/')
    video = models.FileField(upload_to='chapter_videos/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
