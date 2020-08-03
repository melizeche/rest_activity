from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import serializers

from core.models import Actividad, Imagen, Tipo, Origen


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ('image',)


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id', 'texto',)


class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origen
        fields = ('id', 'texto',)


class ActividadSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True, source='imagen_set', read_only=True)

    class Meta:
        model = Actividad
        fields = ('ID', 'tipo', 'origen', 'cuerpo','imagenes')

    def create(self, validated_data):
        actividad = Actividad.objects.create(**validated_data)
        imgs = self.initial_data.getlist('imagenes') 
        for img in imgs:
            if isinstance(img, InMemoryUploadedFile):
                Imagen.objects.create(actividad=actividad, image=img)
        return actividad
