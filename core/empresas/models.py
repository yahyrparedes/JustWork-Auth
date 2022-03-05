from django.db import models
from accounts.models import MyUser

class Empresa(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=255, blank=False)
    ruc = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.razon_social