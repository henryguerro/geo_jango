from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'countries/home.html'

    def get_context_data(self, **kwargs):
        ar = {'name': 'Argentina', 'code': 'AR'}
        co = {'name': 'Colombia', 'code': 'CO'}
        ve = {'name': 'Venezuela', 'code': 'VE'}

        return {'countries': [ar, co, ve]}


class TagsView(TemplateView):
    template_name = 'countries/tags.html'

    def get_context_data(self, **kwargs):
        return {'population': '50'}
