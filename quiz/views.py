from django.http import HttpResponse
from django.template import loader


def home_page(request):
    template = loader.get_template('index.html')
    context = {
        'name': 'Даруся і Мирося',
    }

    return HttpResponse(template.render(context, request))
