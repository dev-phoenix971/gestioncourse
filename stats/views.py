from rest_framework import viewsets
from .models import Trends
from django.shortcuts import render
from .serializers import TrendsSerializer
from django.db.models import Count, Avg, Max, Min, Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from races.models import RaceResult



class TrendsViewSet(viewsets.ModelViewSet):
    queryset = Trends.objects.all()
    serializer_class = TrendsSerializer

class TrendsView(APIView):
    """
    API pour afficher les tendances des critères les plus utilisés.
    """

    def get(self, request):
        trends = Trends.objects.first()
        if not trends:
            return Response({"message": "Pas encore de tendances calculées."}, status=404)
        
        serializer = TrendsSerializer(trends)
        return Response(serializer.data)


def race_statistics(request):
    """
    Génère les statistiques uniquement pour les courses Quinté 2025.
    """
    results = RaceResult.objects.filter(race__date__year=2025, race__location="Vincennes")
    
    # Calcul des stats (exemple : cheval le plus gagnant)
    best_horses = results.values('horse__name').annotate(wins=Count('horse')).order_by('-wins')[:5]

    return render(request, 'statistics/race_statistics.html', {'best_horses': best_horses})