import requests
from typing import Any
from django.core.management.base import BaseCommand
from valutes.models import *

class Command(BaseCommand):
    help = 'Команда для получения и сохранения информации о валюте'

    def handle(self, *args, **options):
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        date = data['Date'].split('T')[0]
        currency = data['Valute']
        for obj in currency.values():
            CharCode = obj['CharCode']
            Name = obj['Name']
            Value = obj['Value']
            a = ValuteInfo(char_code = CharCode, name = Name)
            try:
                a.save()
                currency = a
            except:
                currency = ValuteInfo.objects.get(char_code = CharCode)
            b = ValuteRateInfo(currency = currency, date = date, value = Value)
            if len(ValuteRateInfo.objects.filter(currency = currency, date = date, value = Value))==0:
                b.save()
                


