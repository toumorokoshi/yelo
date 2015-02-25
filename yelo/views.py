from django.contrib.auth.models import User, Group
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from yelo.models import Elo
from yelo.serializers import (
    EloSerializer,
    GroupSerializer,
    UserSerializer
)

# Create your views here.


def index(request):
    return render(request, "index.html", {
        'title': 'yelo'
    })


def ratings(request):
    elo_ratings = Elo.objects.order_by('elo')
    return JsonResponse({
        'ratings': [model_to_dict(e, fields=['elo', 'player']) for e in elo_ratings]
    })


class EloViewSet(viewsets.ModelViewSet):

    queryset = Elo.objects.all()
    serializer_class = EloSerializer


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
