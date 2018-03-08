
def countries_data(request):
    ar = {'name': 'Argentina', 'code': 'AR'}
    co = {'name': 'Colombia', 'code': 'CO'}
    ve = {'name': 'Venezuela', 'code': 'VE'}

    return {'countries': [ar, co, ve], 'population': 50}