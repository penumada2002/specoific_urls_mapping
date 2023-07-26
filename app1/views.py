from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def anu(requst):
    return HttpResponse('<h1> this is my frist project...</h1>')
