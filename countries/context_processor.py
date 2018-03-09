from django.urls import reverse
from .models import Country


def countries_data(request):
    countries = Country.objects.all()

    return {'countries': countries, 'population': 50}
