from rest_framework import viewsets
from .models import Prediction
from .serializers import PredictionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UserPredictionPreferences
from .serializers import UserPredictionPreferencesSerializer
import uuid

class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer


class UserPredictionPreferencesView(APIView):
    """
    Vue API pour gérer les préférences de prédiction des utilisateurs.
    Les préférences sont stockées temporairement pour une session anonyme.
    """

    def get(self, request):
        # Récupérer ou générer un identifiant unique (stocké dans un cookie)
        session_id = request.COOKIES.get('session_id')
        if not session_id:
            session_id = str(uuid.uuid4())  # Générer un ID anonyme
            response = Response({"message": "Session créée", "session_id": session_id})
            response.set_cookie("session_id", session_id, max_age=7*24*60*60)  # Expire après 7 jours
            return response

        # Chercher les préférences existantes
        preferences, created = UserPredictionPreferences.objects.get_or_create(session_id=session_id)
        serializer = UserPredictionPreferencesSerializer(preferences)
        return Response(serializer.data)

    def post(self, request):
        session_id = request.COOKIES.get('session_id')
        if not session_id:
            return Response({"error": "Session ID requis"}, status=status.HTTP_400_BAD_REQUEST)

        preferences, created = UserPredictionPreferences.objects.get_or_create(session_id=session_id)
        serializer = UserPredictionPreferencesSerializer(preferences, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)