from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, MindTree 4 Th April World!")
