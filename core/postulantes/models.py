from django.db import models
from accounts.models import MyUser

class Postulante(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, blank=False)
    apellidos = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.nombre