from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def about(request):
    return render(request, template_name='index.html')


def contact(request):
    return render(request, template_name='index.html')


def signup(request):
    return render(request, template_name='index.html')
