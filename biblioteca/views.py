from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Livros
from .serializers import LivroSerializer
from .models import Alunos
from .serializers import AlunoSerializer
from .models import Emprestimos
from .serializers import EmprestimoSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivroSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimoSerializer