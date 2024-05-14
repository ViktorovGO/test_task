from django.http import JsonResponse, Http404
from django.core import serializers
from .models import *

# Create your views here.

def show_rates(request):

    try:
        date = request.GET['date']
        data = list(ValuteRateInfo.objects.filter(date = date).values())
        if len(data)==0:
            return JsonResponse({'info':'There is no data for this date'}, safe = False)
        for obj in data:
            obj['currency'] = list(ValuteInfo.objects.filter(id = obj['currency_id']).values())
    except:
        raise Http404('Date parameter required')
    
    return JsonResponse(data, safe = False)