from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from yelo.models import Elo
from yelo.serializers import EloSerializer

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
