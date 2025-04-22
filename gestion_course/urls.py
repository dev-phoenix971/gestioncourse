from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from races.views import RaceViewSet, HorseViewSet, JockeyViewSet, RaceResultViewSet
from betting.views import BetViewSet
from predictions.views import PredictionViewSet
from stats.views import TrendsViewSet


router = DefaultRouter()
router.register(r'races', RaceViewSet)
router.register(r'horses', HorseViewSet)
router.register(r'jockeys', JockeyViewSet)
router.register(r'race-results', RaceResultViewSet)
router.register(r'bets', BetViewSet)
router.register(r'predictions', PredictionViewSet)
router.register(r'trends', TrendsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('predictions.urls')),
    path('api/', include('stats.urls')),
    path('', include('races.urls')),
    path('', include('betting.urls')),
]

