from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def testpage(request):
    return HttpResponse("Hello, world. You're on the Test page.")