from django.shortcuts import render


# Create your views here.
def index(request):
    # Page from the theme
    return render(request, 'home.html')
