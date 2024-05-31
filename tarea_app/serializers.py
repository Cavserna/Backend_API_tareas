from rest_framework import serializers
from .models import Tarea

# Serializer para modelar los datos que se envían por las peticiones en la view
class TareaSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ('id', 'nombre', 'descripcion', 'fecha_creacion')
        read_only_fields = ('fecha_creacion',)