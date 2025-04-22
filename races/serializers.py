from rest_framework import serializers
from .models import Race, Horse, Jockey, RaceResult

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'

class HorseSerializer(serializers.ModelSerializer):
    win_ratio = serializers.FloatField(read_only=True)

    class Meta:
        model = Horse
        fields = '__all__'

class JockeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Jockey
        fields = '__all__'

class RaceResultSerializer(serializers.ModelSerializer):
    race = RaceSerializer()
    horse = HorseSerializer()
    jockey = JockeySerializer()

    class Meta:
        model = RaceResult
        fields = '__all__'
