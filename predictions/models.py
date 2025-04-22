from django.db import models
from races.models import Race, Horse
from django.utils import timezone
from datetime import timedelta

class Prediction(models.Model):
    """Modèle stockant les prédictions générées."""
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    probability = models.FloatField(help_text="Probabilité estimée de victoire (%)")
    reason = models.TextField(help_text="Explication détaillée de la prédiction")
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prédiction {self.horse.name} - {self.race.name} ({self.probability}%)"


class UserPreferences(models.Model):
    """Stocke les critères préférés des utilisateurs anonymes pour les tendances."""
    weather_importance = models.FloatField(default=0.5, help_text="Importance de la météo")
    horse_form_importance = models.FloatField(default=0.5, help_text="Importance de la forme du cheval")
    jockey_experience_importance = models.FloatField(default=0.5, help_text="Importance de l'expérience du jockey")
    date_saved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Préférences {self.date_saved.strftime('%d/%m/%Y')}"
    

class UserPredictionPreferences(models.Model):
    """
    Modèle pour stocker temporairement les préférences de prédiction des utilisateurs.
    Les données sont conservées 7 jours.
    """
    session_id = models.CharField(max_length=255, unique=True)  # Identifiant unique anonyme
    weather_importance = models.FloatField(default=0.5)  # Impact météo
    horse_form_importance = models.FloatField(default=0.5)  # Forme du cheval
    jockey_experience_importance = models.FloatField(default=0.5)  # Expérience du jockey
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(days=7)