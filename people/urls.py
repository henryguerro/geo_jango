from django.urls import path
from people.views import register

urlpatterns = [
    path('register/', register, name='people.register')
]