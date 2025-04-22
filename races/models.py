from django.db import models

class Race(models.Model):
    """Modèle représentant une course de chevaux."""
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    distance = models.IntegerField(help_text="Distance en mètres")
    terrain = models.CharField(max_length=50, choices=[("herbe", "Herbe"), ("sable", "Sable"), ("boue", "Boue")])
    weather = models.CharField(max_length=50, help_text="Conditions météo")

    def __str__(self):
        return f"{self.name} - {self.date.strftime('%d/%m/%Y')}"


class Horse(models.Model):
    """Modèle représentant un cheval."""
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=100, help_text="Race du cheval")
    trainer = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    def win_ratio(self):
        """Retourne le pourcentage de victoires."""
        total_races = self.wins + self.losses
        return (self.wins / total_races * 100) if total_races > 0 else 0

    def __str__(self):
        return self.name


class Jockey(models.Model):
    """Modèle représentant un jockey."""
    name = models.CharField(max_length=255)
    experience = models.IntegerField(help_text="Nombre d'années d'expérience")
    win_percentage = models.FloatField(help_text="Pourcentage de victoires")

    def __str__(self):
        return self.name


class RaceResult(models.Model):
    """Stocke les résultats d'une course passée."""
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    jockey = models.ForeignKey(Jockey, on_delete=models.CASCADE)
    position = models.IntegerField()
    time = models.FloatField(help_text="Temps réalisé en secondes")

    class Meta:
        unique_together = ("race", "horse")

    def __str__(self):
        return f"{self.horse.name} - {self.race.name} - Position {self.position}"
