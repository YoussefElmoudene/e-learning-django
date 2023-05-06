import logging
import os

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
from learning_app.models import Course, Teacher, Chapter

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    # Page from the theme
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'courses': courses, 'teachers': teachers})


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
def show_course_chapters(request):
    filter_value = request.GET.get('filter')
    teacher = Teacher.objects.all().get(user_profile=request.user.id)
    courses = Course.objects.all().filter(teacher=teacher)
    print(filter_value)
    if filter_value is None or filter_value == 'all':
        chapters = Chapter.objects.all()
    else:
        chapters = Chapter.objects.all().filter(course=filter_value)

    print(chapters)
    return render(request, "teacher/chapters.html", {'courses': courses, 'chapters': chapters})


@login_required
def show_teacher_create_course(request):
    return render(request, "teacher/create-course.html")


@login_required
def show_teacher_create_chapter(request):
    courses = Course.objects.all()
    return render(request, "teacher/create-chapter.html", {'courses': courses})


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


def create_chapter(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        name = request.POST.get("name")
        description = request.POST.get("description")
        orderNumber = request.POST.get("orderNumber")
        print(request.FILES)
        print(request.POST.get('image'))

        # upload image
        image_file = request.FILES['image']
        image_name = image_file.name.lower().replace(' ', '_')
        img = os.path.join('static/media/chapter_images/', image_name)
        with open(img, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        # upload video
        video_file = request.FILES['video']
        video_name = video_file.name.lower().replace(' ', '_')
        video = os.path.join('static/media/chapter_videos/', video_name)

        with open(video, 'wb+') as destination:
            for chunk in video_file.chunks():
                destination.write(chunk)

        course = Course.objects.all().get(id=request.POST.get('filter'))
        chapter = Chapter(name=name, description=description, orderNumber=orderNumber,
                          img=img, video=video, course=course)
        print(chapter)
        chapter.save()
        print(chapter)
        return redirect("/teacher-create-chapter")
