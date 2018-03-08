from django.shortcuts import render
from django.views.generic import TemplateView


class ContinentsView(TemplateView):
    template_name = 'continents.html'

    def get_context_data(self, *args, **kwargs):
        europe = {'name': 'Europa', 'translate': 'Europe', 'color': 'red'}
        america = {'name': 'América', 'translate': 'america', 'color': 'blue'}
        asia = {'name': 'Asia', 'translate': 'asia', 'color': 'yellow'}

        return {'continents': [europe, america, asia]}
