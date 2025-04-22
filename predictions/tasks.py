from celery import shared_task
from races.models import Race
from .prediction_engine import generate_predictions

@shared_task
def update_predictions():
    """
    Met à jour les prédictions pour toutes les courses disponibles.
    """
    races = Race.objects.filter(date__gte="2024-01-01")  # Filtrer les courses récentes
    for race in races:
        generate_predictions(race)
    
    return f"Prédictions mises à jour pour {races.count()} courses."
