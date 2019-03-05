from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")


def hello2(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
