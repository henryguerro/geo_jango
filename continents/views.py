from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from continents.models import Continent


class ContinentsView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        continents = Continent.objects.all()

        return {'continents': continents}


class ContinentsDetailView(DetailView):
    template_name = 'detail.html'
    model = Continent