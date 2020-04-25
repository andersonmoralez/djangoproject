
from rest_framework import serializers
from .models import EventRegister

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegister
        fields = ('id', 'name', 'sobrenome', 'senha', 'email')

