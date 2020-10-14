from django.shortcuts import render


def home(request):
    return render(request, template_name='index.html')


def works(request):
    return render(request, template_name='index.html')


def description(request, name):
    return render(request, template_name='index.html')


def skills(request):
    return render(request, template_name='index.html')
