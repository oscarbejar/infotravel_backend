from rest_framework import serializers
from .models import Lugares

class LugaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = ('id', 'titulo', 'contenido', 'created', 'updated')

