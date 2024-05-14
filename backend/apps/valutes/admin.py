from django.contrib import admin
from .models import *
# Register your models here.
class ValuteInfoAdmin(admin.ModelAdmin):
    list_display = ('char_code', 'name',)

class ValuteRateInfoAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'value',)

admin.site.register(ValuteInfo, ValuteInfoAdmin)
admin.site.register(ValuteRateInfo, ValuteRateInfoAdmin)