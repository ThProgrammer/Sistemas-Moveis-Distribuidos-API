from rest_framework import viewsets
from livros.api import serializers
from livros import models

class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializer
    queryset = models.Livros.objects.all()

class FilmesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FilmesSerializer
    queryset = models.Filmes.objects.all()

class MusicasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MusicasSerializer
    queryset = models.Musicas.objects.all()


