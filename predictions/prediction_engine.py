from races.models import Race, Horse, Jockey, RaceResult
from predictions.models import Prediction, UserPredictionPreferences
import numpy as np

def calculate_horse_score(horse, session_id=None):
    """
    Calcule un score de performance pour un cheval.
    Plus le score est élevé, plus le cheval a des chances de gagner.
    """
    # Facteurs pris en compte
    win_ratio = horse.win_ratio()  # % de victoires
    recent_results = RaceResult.objects.filter(horse=horse).order_by('-race__date')[:5]  # 5 dernières courses
    jockey = Jockey.objects.filter(name=horse.trainer).first()  # Associer un jockey
    jockey_score = jockey.win_percentage if jockey else 50  # Score du jockey
    recent_positions = [result.position for result in recent_results]

    # Calcul du score global
    avg_position = np.mean(recent_positions) if recent_positions else 5  # Position moyenne
    score = (win_ratio * 0.4) + (100 - avg_position * 10) * 0.3 + (jockey_score * 0.3)

    # Récupérer les préférences de l'utilisateur (ou valeurs par défaut)
    preferences = UserPredictionPreferences.objects.filter(session_id=session_id).first()
    if not preferences:
        preferences = UserPredictionPreferences(weather_importance=0.5, horse_form_importance=0.5, jockey_experience_importance=0.5)

    # Calcul du score basé sur les préférences
    win_ratio = horse.win_ratio()
    jockey = Jockey.objects.filter(name=horse.trainer).first()
    jockey_score = jockey.win_percentage if jockey else 50

    score = (
        (win_ratio * preferences.horse_form_importance * 100) +
        (jockey_score * preferences.jockey_experience_importance) +
        (np.random.randint(70, 100) * preferences.weather_importance)  # Influence météo simulée
    ) / 3  # Normalisation
    
    return round(score, 2)

def generate_predictions(race):
    """
    Génère les prédictions pour une course donnée.
    """
    horses = race.horse_set.all()  # Liste des chevaux dans la course
    predictions = []

    for horse in horses:
        score = calculate_horse_score(horse)
        reason = f"Forme récente : {horse.win_ratio()}%, " \
                 f"Jockey : {horse.trainer}, " \
                 f"Position moyenne : {score}"
        
        # Création d'une prédiction
        prediction = Prediction.objects.create(
            race=race,
            horse=horse,
            probability=score,
            reason=reason
        )
        predictions.append(prediction)
    
    # Trier les prédictions par score décroissant
    predictions.sort(key=lambda x: x.probability, reverse=True)
    return predictions
