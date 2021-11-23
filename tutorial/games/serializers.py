from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()
    gmae_category = serializers.CharField(max_length=200)
    played = serializers.BooleanField(required=False)
    
    def create(self, validated_date):
        return Game.objects.create(**validated_date)
    
    def update(self, instance, validated_date):
        instance.name = validated_date.get('name',instance.name)
        instance.release_date = validated_date.get('release_date', instance.release_date)
        instance.game_category = validated_date.get('game_category', instance.game_category)
        instance.played = validated_date.get('played', instance.played)
        instance.save()
        return instance