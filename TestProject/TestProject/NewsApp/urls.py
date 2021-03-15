from django.urls import path
from .views import News, Home, Contact

urlpatterns = [
    path('news/<int:year>', News, name='News'),
    path('home/', Home, name='Home'),
    path('contact/', Contact, name='Contact'),
]