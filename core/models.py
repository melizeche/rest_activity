import random
import string

from django.db import models


def create_alpha_id(self):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


class Origen(models.Model):
    texto = models.TextField()


class Tipo(models.Model):
    texto = models.TextField()


class Actividad(models.Model):
    ID = models.CharField(primary_key=True, max_length=8, default=create_alpha_id)
    tipo = models.ForeignKey(Tipo)
    origen = models.ForeignKey(Origen)
    cuerpo = models.TextField()


class Imagen(models.Model):
    actividad = models.ForeignKey(Actividad)
    image = models.ImageField(upload_to='images')
