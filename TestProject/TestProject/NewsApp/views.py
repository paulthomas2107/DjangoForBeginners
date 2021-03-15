from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import News as NewsData

# Create your views here.


def Home(request):
    context = {
        "name": "Paul Thomas",
        "number": 217662020,
    }
    return render(request, 'index.html', context)


def News(request):

    obj = NewsData.objects.get(id=1)

    context = {
        "data": obj
    }

    return render(request, 'news.html', context)


def Contact(request):
    return render(request, 'contact.html')