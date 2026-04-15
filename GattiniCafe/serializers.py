from rest_framework import serializers
from .models import Categoria, Prodotto
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdottoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodotto
        fields = '__all__'

# Richiesta JSON --> utente Django
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # VALIDAZIONE DATI
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    # CREA UTENTE DB
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        # RITORNA LA RISPOSTA
        return user