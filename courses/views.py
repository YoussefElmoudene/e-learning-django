from django.shortcuts import render

from learning_app.models import Course


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
