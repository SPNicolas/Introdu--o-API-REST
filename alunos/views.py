from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Estado
from .serializers import EstadoSerializer
from .models import Cidade
from .serializers import CidadeSerializer
from .models import Aluno
from .serializers import AlunoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
