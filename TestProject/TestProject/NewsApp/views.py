from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def Home(request):
    context = {
        "name": "Paul Thomas",
        "number": 217662020,
    }
    return render(request, 'index.html', context)


def News(request):
    context = {
        "list": ['Paul', 'Caitlin', 'Rory', 'Scruffy', 'Jaws'],
        "mynum": 150,
    }
    return render(request, 'news.html', context)


def Contact(request):
    return render(request, 'contact.html')