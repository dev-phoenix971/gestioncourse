from rest_framework import viewsets
from .models import Race, Horse, Jockey, RaceResult
from .serializers import RaceSerializer, HorseSerializer, JockeySerializer, RaceResultSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Race, Horse, RaceResult
from predictions.models import Prediction
from .forms import RaceForm, HorseForm, RaceResultForm, RaceUpdateForm, HorseUpdateForm

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class HorseViewSet(viewsets.ModelViewSet):
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer

class JockeyViewSet(viewsets.ModelViewSet):
    queryset = Jockey.objects.all()
    serializer_class = JockeySerializer

class RaceResultViewSet(viewsets.ModelViewSet):
    queryset = RaceResult.objects.all()
    serializer_class = RaceResultSerializer


def race_list(request):
    races = Race.objects.order_by('-date') # Trier par date décroissante
    predictions = Prediction.objects.all().order_by('-probability')[:10]  # Top 10

    return render(request, 'races/race_list.html', {'races': races, 'predictions': predictions})


def add_race(request):
    if request.method == "POST":
        form = RaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('race_list')  # Redirection après ajout
    else:
        form = RaceForm()

    return render(request, 'races/add_race.html', {'form': form})


def add_horse(request):
    """
    Vue pour ajouter un cheval manuellement.
    """
    if request.method == "POST":
        form = HorseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horse_list')  # Redirige vers la liste des chevaux
    else:
        form = HorseForm()

    return render(request, 'races/add_horse.html', {'form': form})



def add_race_result(request):
    """
    Vue pour ajouter manuellement un résultat de course.
    """
    if request.method == "POST":
        form = RaceResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('race_list')  # Redirige vers la liste des courses
    else:
        form = RaceResultForm()

    return render(request, 'races/add_race_result.html', {'form': form})


def horse_list(request):
    """
    Affiche la liste des chevaux.
    """
    horses = Horse.objects.all()
    return render(request, 'races/horse_list.html', {'horses': horses})


def update_race(request, race_id):
    """
    Vue pour modifier une course existante.
    """
    race = get_object_or_404(Race, id=race_id)
    
    if request.method == "POST":
        form = RaceUpdateForm(request.POST, instance=race)
        if form.is_valid():
            form.save()
            return redirect('race_list')  # Rediriger après modification
    else:
        form = RaceUpdateForm(instance=race)

    return render(request, 'races/update_race.html', {'form': form, 'race': race})


def delete_race(request, race_id):
    """
    Vue pour supprimer une course.
    """
    race = get_object_or_404(Race, id=race_id)
    race.delete()
    return redirect('race_list')  # Redirection après suppression


def update_horse(request, horse_id):
    """
    Vue pour modifier un cheval existant.
    """
    horse = get_object_or_404(Horse, id=horse_id)
    
    if request.method == "POST":
        form = HorseUpdateForm(request.POST, instance=horse)
        if form.is_valid():
            form.save()
            return redirect('horse_list')  # Redirection après modification
    else:
        form = HorseUpdateForm(instance=horse)

    return render(request, 'races/update_horse.html', {'form': form, 'horse': horse})


def delete_horse(request, horse_id):
    """
    Vue pour supprimer un cheval.
    """
    horse = get_object_or_404(Horse, id=horse_id)
    horse.delete()
    return redirect('horse_list')  # Redirection après suppression

def home(request):
    """
    Vue pour la page d'accueil de l'application.
    """
    return render(request, 'races/home.html')

