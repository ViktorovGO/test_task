from django.urls import path
from .views import show_rates

urlpatterns = [
    path('show_rates/', show_rates),
]
