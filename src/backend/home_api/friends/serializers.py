
from friends.models import Friendship
from rest_framework import serializers

from django.contrib.auth.models import User

class FriendshipSerializer(serializers.ModelSerializer):

    user1 = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    user2 = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Friendship
        fields = ['id', 'user1', 'user2', 'status', 'created_at']


    def create(self, validated_data):
        return Friendship.objects.create(**validated_data)