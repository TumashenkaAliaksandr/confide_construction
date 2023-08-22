from django.shortcuts import render


def index(request):
    return render(request, 'webapp/index-2.html')


def about(request):
    return render(request, 'webapp/about-us.html')

def contacts(request):
    return render(request, 'webapp/contact-us-1.html')
