from django.db import models

class Trends(models.Model):
    """Stocke les tendances des critères les plus utilisés par les utilisateurs."""
    criteria = models.CharField(max_length=100, help_text="Critère analysé")
    selection_count = models.IntegerField(default=0, help_text="Nombre de fois utilisé")
    weather_avg = models.FloatField(default=0.5)  # Moyenne d'importance de la météo
    horse_form_avg = models.FloatField(default=0.5)  # Moyenne de l'importance de la forme du cheval
    jockey_exp_avg = models.FloatField(default=0.5)  # Moyenne de l'expérience du jockey
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tendances mises à jour le {self.updated_at.strftime('%d/%m/%Y')}"

    def __str__(self):
        return f"Tendance - {self.criteria}: {self.selection_count} sélections"
