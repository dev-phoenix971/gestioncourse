from rest_framework import viewsets
from .models import Bet
from .serializers import BetSerializer
from django.shortcuts import render, redirect
from .forms import BetForm


class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer


def place_bet(request):
    """
    Vue pour placer un pari sur le Quinté 2025.
    """
    if request.method == "POST":
        form = BetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bet_list')  # Redirection vers la liste des paris
    else:
        form = BetForm()

    return render(request, 'betting/place_bet.html', {'form': form})