from django.db import models
from django.utils import timezone
from datetime import timedelta
from races.models import Race, Horse

class Bet(models.Model):
    """Modèle représentant un pari simulé."""
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    selected_horses = models.ManyToManyField(Horse)
    bet_type = models.CharField(
        max_length=50,
        choices=[
            ("simple_gagnant", "Simple Gagnant"),
            ("simple_place", "Simple Placé"),
            ("tierce", "Tiercé"),
            ("quarte", "Quarté"),
            ("quinte", "Quinté")
        ]
    )
    amount = models.FloatField(help_text="Montant misé (simulation)")
    potential_gain = models.FloatField(default=0.0, help_text="Gain potentiel simulé")
    timestamp = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        """Vérifie si le pari doit être supprimé après 7 jours."""
        return timezone.now() > self.timestamp + timedelta(days=7)

    def __str__(self):
        return f"Pari {self.bet_type} sur {self.race.name} - {self.timestamp.strftime('%d/%m/%Y')}"

