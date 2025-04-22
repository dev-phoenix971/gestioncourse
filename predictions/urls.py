from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PredictionViewSet, UserPredictionPreferencesView

router = DefaultRouter()
router.register(r'predictions', PredictionViewSet, basename='prediction')

urlpatterns = [
    path('', include(router.urls)),
    path('api/user-preferences/', UserPredictionPreferencesView.as_view(), name="user_preferences"),
]
