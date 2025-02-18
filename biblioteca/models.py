from django.db import models

class Livros (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ano_publicacao = models.DateField()


    def __str__(self):
        return self.id, self.titulo, self.autor, self.ano_publicacao

class Alunos (models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)


    def __str__(self):
        return self.id, self.nome, self.matricula, self.curso

class Emprestimos (models.Model):
    id = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.PROTECT)
    id_livro = models.ForeignKey(Livros, on_delete=models.PROTECT)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    
    def __str__(self):
        return self.id, self.id_aluno, self.id_livro, self.data_emprestimo, self.data_devolucao
