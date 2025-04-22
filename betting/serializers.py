from rest_framework import serializers
from .models import Bet

class BetSerializer(serializers.ModelSerializer):
    race = serializers.StringRelatedField()
    selected_horses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Bet
        fields = '__all__'
