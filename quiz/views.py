from django.http import HttpResponse
from django.template import loader
from django.contrib.sites.shortcuts import get_current_site


def home_page(request):
    template = loader.get_template('index.html')
    context = {
        'name': 'Даруся і Мирося',
    }

    return HttpResponse(template.render(context, request))


def greet(request):
    baseUrl = get_current_site(request).domain
    greetName = request.POST.get('greet_name')
    template = loader.get_template('greet.html')
    context = {
        'name': greetName,
        'baseUrl': "http://" + baseUrl
    }

    return HttpResponse(template.render(context, request))
