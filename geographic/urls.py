"""geographic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from countries.views import HomeView, CountriesSearchView, CountryIdDetailView
from continents.views import ContinentsView, ContinentsDetailView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin.index'),
    path("", HomeView.as_view(), name='countries.index'),
    path('people/', include('people.urls')),
    path('countries/', include('countries.urls')),
    path("continents/", ContinentsView.as_view(), name='continents.index'),
    path("continents/<int:pk>", ContinentsDetailView.as_view(), name='continents.detail'),
]
