from django.contrib import admin
from .models import News, SportsNews, RegistrationData, Publication, Article, Article2, Reporter

# Register your models here.
admin.site.register(News)
admin.site.register(SportsNews)
admin.site.register(RegistrationData)
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Article2)
admin.site.register(Reporter)


