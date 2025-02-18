from rest_framework.serializers import ModelSerializer
from .models import Livros, Alunos, Emprestimos

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Alunos
        fields = '__all__'

class EmprestimoSerializer(ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = '__all__'