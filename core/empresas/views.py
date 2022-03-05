from rest_framework import viewsets

from .models import Empresa
from .serializers import EmpresaSerializer

class EmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    model = Empresa
