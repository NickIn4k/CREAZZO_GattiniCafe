from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import (ProdottoSerializer, CategoriaSerializer, RegisterSerializer)
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Prodotto
from .models import Categoria
from .serializers import RegisterSerializer

# IN QUESTO CODICE CI SONO ANCHE DEGLI APPUNTI
# SU NUOVI ELEMENTI NON VISTI IN CLASSE

# DEBUG - (VIEW COME NEL PRIMO TUTORIAL)
class AllProducts(ListView):
    model = Prodotto
    template_name = "prodotti/index.html"

class AllCategories(ListView):
    model = Categoria
    template_name = "categorie/index.html"

# VIEW RICHIESTE DALLA CONSEGNA

# LISTA PRODOTTI CON PARAMETRI AGGIUNTIVI - NON VISTO IN CLASSE
class ProdottoList(ListAPIView):
    serializer_class = ProdottoSerializer

    # Check dati da Query String
    def get_queryset(self):
        queryset = Prodotto.objects.all()

        categoria = self.request.query_params.get('categoria')
        disponibile = self.request.query_params.get('disponibile')
        search = self.request.query_params.get('search')

        if categoria:
            queryset = queryset.filter(categoria_id=categoria)

        if disponibile:
            if disponibile.lower() == 'true':
                queryset = queryset.filter(disponibile=True)

        if search:
            # Q: QUERY COMPLESSE (BOOLEAN OP)
            queryset = queryset.filter(
                Q(nome__icontains=search) |Q(descrizione__icontains=search)
            )

        return queryset

# PRODOTTO SINGOLO <int:id>
class ProdottoDetail(RetrieveAPIView):
    queryset = Prodotto.objects.all()
    serializer_class = ProdottoSerializer
    lookup_field = 'id'

# LISTA CATEGORIE (NO FILTRI RICHIESTI)
class CategoriaList(ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# CATEGORIA SINGOLA <int:id>
class CategoriaDetail(RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    lookup_field = 'id'

# REGISTRAZIONE
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []  # vuoto => nessun permesso richiesto

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })