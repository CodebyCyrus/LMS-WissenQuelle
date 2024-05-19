from rest_framework import serializers
from userauths.models import Profile, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
             model = Profile
             fields = "__all__"