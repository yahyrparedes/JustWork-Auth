from django.contrib import admin
from .models import Empresa

# Register your models here.

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass