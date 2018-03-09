from django.shortcuts import render
from django.views.generic import TemplateView

from continents.models import Continent


class ContinentsView(TemplateView):
    template_name = 'continents.html'

    def get_context_data(self, *args, **kwargs):
        continents = Continent.objects.all()

        return {'continents': continents}
