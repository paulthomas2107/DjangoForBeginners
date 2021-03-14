from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def Home(request):
    return HttpResponse("<h1>This is home.</h1>")


def News(request):
    return HttpResponse("<h1>Latest News for Paul...</h1>")


def Contact(request):
    return HttpResponse("<h1>Contact Details</h1>")