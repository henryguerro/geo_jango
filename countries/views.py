from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import TemplateView, ListView

from countries.forms import CountryCreateFormModel
from countries.models import Country


class HomeView(TemplateView):
    template_name = 'countries/index.html'


class TagsView(TemplateView):
    template_name = 'countries/tags.html'


class CountryIdDetailView(TemplateView):
    template_name = 'countries/detail.html'

    def get_context_data(self, *args, **kwargs):
        code_id = kwargs['id']
        # try:
        #     country = Country.objects.get(id=code_id)
        # except Country.DoesNotExist as e:
        #     raise Http404('The Country {} does no exist'.format(kwargs['id']))
        country = get_object_or_404(Country, id=code_id)
        return {'country': country}


class CountriesSearchView(ListView):
    template_name = 'countries/search.html'
    model = Country

    def get_queryset(self):
        query = self.kwargs['query']

        return Country.objects.filter(name__contains=query)


class CreateCountryView(TemplateView):
    template_name = 'countries/create.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = CountryCreateFormModel(request.POST or None)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        return {'form': self.form}

    def post(self, request, *args, **kwargs):

        if self.form.is_valid():
            country = self.form.save()
            return JsonResponse({'name': country.name})
        return self.get(request, *args, **kwargs)