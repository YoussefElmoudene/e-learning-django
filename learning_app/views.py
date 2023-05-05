import logging

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import window
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from learning_app.auth.Authentication import Authentication
from learning_app.models import Course, Teacher

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    # Page from the theme
    return render(request, 'home.html')


def show_login_page(request):
    return render(request, "login.html")


@login_required
def show_teacher(request):
    return render(request, "teacher/dashboard.html")


@login_required
def show_teacher_courses(request):
    teacher = Teacher.objects.all().get(user_profile=request.user.id)
    all_courses = Course.objects.all().filter(teacher=teacher)
    print(all_courses)
    paginator = Paginator(all_courses, 10)
    page = request.GET.get('page', 1)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(page)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    print(courses)
    return render(request, "teacher/courses.html", {'courses': courses})


@login_required
def show_teacher_create_course(request):
    return render(request, "teacher/create-course.html")


def logout_view(request):
    logout(request)
    return redirect('login')


def do_login(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = Authentication.authenticate(request, username, password)
        print(user)
        if user != None:
            login(request, user)
            if user.role == 'STUDENT':
                return redirect('/student-dashboard')
            elif user.role == 'TEACHER':
                return redirect("/teacher-dashboard")
            else:
                return redirect(reverse("/admin"))
        else:
            messages.error(request, "Invalid Login Details")
            return redirect("/login")


def create_course(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        title = request.POST.get("title")
        level = request.POST.get("level")
        description = request.POST.get("description")
        duration = request.POST.get("duration")
        price = request.POST.get("price")
        oldPrice = request.POST.get("oldPrice")
        teacher = Teacher.objects.all().get(user_profile=request.user.id)
        course = Course(title=title, level=level, description=description, duration=duration, price=price,
                        oldPrice=oldPrice, teacher=teacher)
        course.save()
        print(course)

        return redirect("/teacher-create-course")
