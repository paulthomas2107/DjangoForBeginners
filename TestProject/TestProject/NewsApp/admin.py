from django.contrib import admin
from .models import News, SportsNews, RegistrationData, Publication, Article, Article2, Reporter, Place, Restaurant\
    , Article3, Customer, Staff, AnotherPlace, AnotherRestaurant, MyUser

# Register your models here.
admin.site.register(News)
admin.site.register(SportsNews)
admin.site.register(RegistrationData)
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Article2)
admin.site.register(Reporter)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Article3)
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(AnotherPlace)
admin.site.register(AnotherRestaurant)
admin.site.register(MyUser)

