from django.urls import path
from .views import place_bet

urlpatterns = [
    path('place-bet/', place_bet, name='place_bet'),
]
