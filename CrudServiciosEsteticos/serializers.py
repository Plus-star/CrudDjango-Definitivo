from rest_framework import serializers
from .models import ServiciosEsteticos

class ServiciosEsteticosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosEsteticos
        fields = ('id', '_nombre_servicio', '_descripcion', '_duracion', '_precio')