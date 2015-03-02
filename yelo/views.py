import json
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from yelo.lib.elo_utils import play_match
from yelo.lib.http import api_error
from yelo.models import Elo, Match
from yelo.serializers import (
    EloSerializer,
    MatchSerializer,
    GroupSerializer,
    UserSerializer
)

# Create your views here.


def index(request):
    return render(request, "index.html", {
        'title': 'yelo'
    })


@csrf_exempt
def record_match(request):
    if request.method != 'POST':
        return api_error('record_match must be called as a POST')

    form = json.loads(request.body.decode('utf-8'))

    winner = User.objects.get(username=form['winner'])
    winner_elo = winner.elo.elo

    loser = User.objects.get(username=form['loser'])
    loser_elo = loser.elo.elo

    new_winner_elo, new_loser_elo = play_match(winner_elo, loser_elo)

    match = Match(
        winner=winner,
        winner_before_elo=winner_elo,
        winner_after_elo=new_winner_elo,
        loser=loser,
        loser_before_elo=loser_elo,
        loser_after_elo=new_loser_elo
    )
    match.save()

    winner.elo.elo = new_winner_elo
    winner.elo.save()

    loser.elo.elo = new_loser_elo
    loser.elo.save()

    return JsonResponse({
        'success': True
    })


class EloViewSet(viewsets.ModelViewSet):

    queryset = Elo.objects.all()
    serializer_class = EloSerializer
    ordering = ('-elo',)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MatchViewSet(viewsets.ModelViewSet):

    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    ordering = ('-match_date',)
