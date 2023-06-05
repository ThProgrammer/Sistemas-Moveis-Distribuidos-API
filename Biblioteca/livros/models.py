from django.db import models
from uuid import uuid4

# Create your models here.


class Livros(models.Model):
    id_livros = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    paginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    criado_em = models.DateField(auto_now_add=True)

class Musicas(models.Model):
    id_musicas = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    idioma = models.CharField(max_length=50)
    duracao = models.IntegerField()
    criado_em = models.DateField(auto_now_add=True) 

class Filmes(models.Model):
    id_filmes = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    idioma = models.CharField(max_length=50)
    duracao = models.IntegerField()
    producao = models.CharField(max_length=255)
    criado_em = models.DateField(auto_now_add=True)