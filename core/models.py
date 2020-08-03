import random
import string

from django.db import models


def create_alpha_id():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


class Origen(models.Model):
    texto = models.TextField()

    class Meta:
        verbose_name_plural = 'Origenes'

    def __str__(self):
        return self.texto


class Tipo(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto


class Actividad(models.Model):
    ID = models.CharField(primary_key=True, max_length=8, default=create_alpha_id, editable=False)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    origen = models.ForeignKey(Origen, on_delete=models.CASCADE)
    cuerpo = models.TextField()

    class Meta:
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return f'<Actividad {self.ID}: {self.cuerpo}>'


class Imagen(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = 'Imágenes'

    def __str__(self):
        return f'<Imagen {self.image}: {self.actividad}>'
