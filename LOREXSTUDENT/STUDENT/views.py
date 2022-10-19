from django.shortcuts import render
from django.http import HttpResponese


def home(request):
    return HttpRespones('Hello World')


# Create your views here.
