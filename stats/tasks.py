from celery import shared_task
from predictions.models import UserPredictionPreferences
from .models import Trends

@shared_task
def update_trends():
    """
    Met à jour les tendances des critères les plus utilisés.
    """
    preferences = UserPredictionPreferences.objects.all()

    if not preferences.exists():
        return "Aucune donnée disponible pour calculer les tendances."

    weather_avg = sum([p.weather_importance for p in preferences]) / preferences.count()
    horse_form_avg = sum([p.horse_form_importance for p in preferences]) / preferences.count()
    jockey_exp_avg = sum([p.jockey_experience_importance for p in preferences]) / preferences.count()

    # Mettre à jour ou créer l'enregistrement des tendances
    trends, created = Trends.objects.get_or_create(id=1)
    trends.weather_avg = round(weather_avg, 2)
    trends.horse_form_avg = round(horse_form_avg, 2)
    trends.jockey_exp_avg = round(jockey_exp_avg, 2)
    trends.save()

    return f"Tendances mises à jour : Météo ({weather_avg}), Forme ({horse_form_avg}), Jockey ({jockey_exp_avg})"
