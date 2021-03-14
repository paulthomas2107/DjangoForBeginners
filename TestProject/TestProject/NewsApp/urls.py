from django.urls import path
from .views import News, Home, Contact

urlpatterns = [
    path('news/', News, name='News'),
    path('home/', Home, name='Home'),
    path('contact/', Contact, name='Contact'),
]