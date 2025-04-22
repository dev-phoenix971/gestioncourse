from rest_framework import serializers
from .models import Trends

class TrendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trends
        fields = ['weather_avg', 'horse_form_avg', 'jockey_exp_avg', 'updated_at']