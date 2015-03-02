from django.contrib.auth.models import User, Group
from rest_framework import serializers
from yelo.models import Elo, Match


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class EloSerializer(serializers.ModelSerializer):

    player = UserSerializer()

    class Meta:
        model = Elo
        fields = ('elo', 'player')

    def create(self, validated_data):
        user = User(**validated_data['player'])
        user.save()
        elo = Elo(player=user)
        elo.save()
        return elo


class MatchSerializer(serializers.ModelSerializer):

    loser = UserSerializer()
    winner = UserSerializer()

    class Meta:
        model = Match
        field = (
            'winner',
            'winner_before_elo',
            'winner_after_elo',
            'loser',
            'loser_before_elo',
            'loser_after_elo',
            'match_date',
        )
