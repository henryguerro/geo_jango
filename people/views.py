from django.http import JsonResponse
from django.shortcuts import render
from people.forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        return JsonResponse(form.cleaned_data)
    return render(request, 'people/register.html', {'form': form})

    if request.method == 'GET':
        return render(request, 'people/register.html', {'form': form})
    return JsonResponse(request.POST)
