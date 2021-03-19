from django.shortcuts import render, redirect
from .models import News as NewsData
from .forms import RegistrationForm
from .models import RegistrationData
from django.contrib import messages

# Create your views here.


def register(request):
    context = {
        "form": RegistrationForm
    }
    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        myregister = RegistrationData(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password'],
                                      email=form.cleaned_data['email'],
                                      phone=form.cleaned_data['phone'])
        myregister.save()
        messages.add_message(request, messages.SUCCESS, "You have signed up successfully")

    return redirect('register')


def Home(request):
    context = {
        "name": "Paul Thomas",
        "number": 217662020,
    }
    return render(request, 'index.html', context)


def News(request, year):

    obj = NewsData.objects.get(id=1)

    context = {
        "data": obj
    }

    article_list = NewsData.objects.filter(timestamp__year=year)

    context = {
        'year': year,
        'article_list': article_list
    }

    return render(request, 'news.html', context)


def Contact(request):
    return render(request, 'contact.html')