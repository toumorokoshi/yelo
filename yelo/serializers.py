from django.contrib.auth.models import User, Group
from rest_framework import serializers
from yelo.models import Elo


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
