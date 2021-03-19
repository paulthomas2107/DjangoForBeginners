from django.urls import path
from .views import Home, Contact, register, addUser, modelform, addModalForm

urlpatterns = [

    # path('news/<int:year>', News, name='News'),
    path('home/', Home, name='Home'),
    path('contact/', Contact, name='Contact'),
    path('signup/', register, name='register'),
    path('addUser/', addUser, name='addUser'),
    path('modalform/', modelform, name='form'),
    path('addmodalform/', addModalForm, name='modalform'),

]
