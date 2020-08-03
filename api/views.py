from django.shortcuts import render
from rest_framework import generics, mixins, viewsets

from core.models import Actividad

from .serializers import ActividadSerializer


class ActividadList(generics.ListCreateAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer


class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
