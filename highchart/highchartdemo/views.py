from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.db.models import Count, Q
from .models import Passenger
import json

# Create your views here.

class TitanicChartTemplateView(TemplateView):
    template_name = 'titanic_chart.html'

    def get(self, request):
        dataset = Passenger.objects \
        .values('pclass') \
        .annotate(survived_count=Count('pclass', filter=Q(survived=True)),
                  not_survived_count=Count('pclass', filter=Q(survived=False))) \
        .order_by('pclass')

        categories = list()
        survived_series_data = list()
        not_survived_series_data = list()

        for entry in dataset:
            categories.append('%s Class' % entry['pclass'])
            survived_series_data.append(entry['survived_count'])
            not_survived_series_data.append(entry['not_survived_count'])

        survived_series = {
            'name': 'Survived',
            'data': survived_series_data,
            'color': 'green'
        }

        not_survived_series = {
            'name': 'Survived',
            'data': not_survived_series_data,
            'color': 'red'
        }

        chart = {
            'chart': {'type': 'column'},
            'title': {'text': 'Titanic Survivors by Ticket Class'},
            'xAxis': {'categories': categories},
            'series': [survived_series, not_survived_series]
        }

        dump = json.dumps(chart)

        return render(request, 'titanic_chart.html', {'chart': dump})