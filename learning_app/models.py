from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20)


class Meta:
    abstract = True


class Student(User):
    level = models.CharField(max_length=20)


class Teacher(User):
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
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


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
