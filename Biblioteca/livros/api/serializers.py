from rest_framework import serializers
from livros import models

class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Livros
        fields = '__all__'

class MusicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Musicas
        fields = '__all__'

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Filmes
        fields = '__all__'

