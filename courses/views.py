from django.shortcuts import render


def courses(request):
    # Page from the theme
    return render(request, 'courses.html')
