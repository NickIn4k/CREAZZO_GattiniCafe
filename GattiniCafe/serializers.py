from rest_framework import serializers
from .models import Categoria, Prodotto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodotto
        fields = '__all__'