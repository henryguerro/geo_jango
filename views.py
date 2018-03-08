from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'countries/home.html')


