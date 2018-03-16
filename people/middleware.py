import random

from django.http import Http404


class SecretMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #Antes de vista
        if not request.GET.get('token') or request.GET.get('token') != 'secret':
            raise Http404()

        response = self.get_response(request)
        #Despues de Vista
        return response

class ABMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'testab' not in request.session:
            request.session['testab'] = random.choice(['a', 'b'])

        response = self.get_response(request)
        #Despues de Vista
        return response