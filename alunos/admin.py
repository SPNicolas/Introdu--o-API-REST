from django.contrib import admin
from .models import Estado, Cidade, Aluno

admin.site.register(Aluno)

admin.site.register(Cidade)

admin.site.register(Estado)