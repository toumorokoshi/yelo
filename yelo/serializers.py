from rest_framework import serializers
from yelo.models import Elo


class EloSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Elo
        fields = ('elo', 'player')
