from django.shortcuts import render


def navbar(request):
    # Page from the theme
    return render(request, 'navbar.html')
