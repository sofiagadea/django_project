from django.shortcuts import render
from django.http import HttpResponse

def simple_view(request):
    return HttpResponse("hola")

def homepage(request):
    return HttpResponse("homepage")