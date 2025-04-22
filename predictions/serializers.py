from rest_framework import serializers
from .models import Prediction, UserPredictionPreferences

class PredictionSerializer(serializers.ModelSerializer):
    race = serializers.StringRelatedField()
    horse = serializers.StringRelatedField()

    class Meta:
        model = Prediction
        fields = '__all__'


class UserPredictionPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPredictionPreferences
        fields = ['session_id', 'weather_importance', 'horse_form_importance', 'jockey_experience_importance']
