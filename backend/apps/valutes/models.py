from django.db import models


class ValuteInfo(models.Model):
    char_code = models.CharField(max_length = 15, verbose_name = 'Тикер', unique = True)
    name = models.CharField(max_length = 100, verbose_name = 'Название валюты')

    def __str__(self) -> str:
        return self.char_code
    
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'
        ordering = ['char_code']

class ValuteRateInfo(models.Model):
    currency = models.ForeignKey('ValuteInfo', on_delete = models.CASCADE, verbose_name = 'Валюта')
    date = models.DateField(verbose_name = 'Дата сбора данных')
    value = models.FloatField(verbose_name = 'Курс')

    class Meta:
        verbose_name = 'Курсы валют'
        verbose_name_plural = 'Курсы валют'
        ordering = ['currency']
