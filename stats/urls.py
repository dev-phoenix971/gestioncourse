from django.urls import path
from .views import TrendsView, race_statistics

urlpatterns = [
    path('trends/', TrendsView.as_view(), name="trends"),
    path('race-statistics/', race_statistics, name='race_statistics'),
]
