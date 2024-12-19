from rest_framework import serializers
from .models import Villa, Visit
from rest_framework import serializers
from .models import Villa
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = ['id', 'nom', 'description', 'prix', 'disponible', 'emplacement', 'lien_visite', 'image']




class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

