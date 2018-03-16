from django.urls import path
from countries.views import HomeView, \
    CountryIdDetailView, \
    CountriesSearchView, \
    CreateCountryView

urlpatterns = [
    path("", HomeView.as_view(), name='countries.index'),
    path("<int:id>", CountryIdDetailView.as_view(), name='countries.detail'),
    path("create", CreateCountryView.as_view(), name='countries.create'),
    path("search/<query>", CountriesSearchView.as_view(), name='countries.search'),
]