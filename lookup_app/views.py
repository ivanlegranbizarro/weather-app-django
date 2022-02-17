from django.shortcuts import render

# Create your views here.


def home(request):
    import json
    import requests

    if request.method == 'POST':
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='
            + zipcode +
            '&distance=5&API_KEY=DD9CC46E-CE95-4051-83EB-63283D2535AD')
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error'
        return render(request, 'lookup_app/home.html', {
            'api': api,
            'zipcode': zipcode
        })

    api_request = requests.get(
        'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=DD9CC46E-CE95-4051-83EB-63283D2535AD'
    )
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Error'

    return render(request, 'lookup_app/home.html', {'api': api})


def about(request):
    return render(request, 'lookup_app/about.html')