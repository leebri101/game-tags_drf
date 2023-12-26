from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'created_at', 'updated_at', 'user_name', 'first_name',
            'last_name', 'bio', 'avatar', 'favourite_games',
            ]
