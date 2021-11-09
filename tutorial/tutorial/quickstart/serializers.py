from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']