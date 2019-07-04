from rest_framework import serializers
from .models import Attractions

class AttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attractions
        fields = ['id', 'name', 'description']