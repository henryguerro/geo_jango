from django.http import JsonResponse
from django.shortcuts import render
from people.forms import RegisterForm, RegisterFormModel
from people.models import Person


def register(request):
    fathers = Person.objects.filter(children__isnull=True)
    form = RegisterFormModel(fathers, request.POST or None)

    if form.is_valid():
        # data = form.cleaned_data
        #
        # person = Person.objects.create(first_name=data['first_name'], father=data['father'])
        #
        # for country in data['nationality']:
        #     person.nationality.add(country)

        person = form.save()

        return JsonResponse({
            'name': person.first_name,
            'father': str(person.father),
            'nationality': ','.join([str(country) for country in person.nationality.all()])
        })
    return render(request, 'people/register.html', {'form': form})

    # if request.method == 'GET':
    #     return render(request, 'people/register.html', {'form': form})
    # return JsonResponse(request.POST)
