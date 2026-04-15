from django.urls import path
from .views import ProdottoList, ProdottoDetail, CategoriaList, CategoriaDetail, RegisterView, MeView

urlpatterns = [
    path('prodotti/', ProdottoList.as_view()),
    path('prodotti/<int:id>/', ProdottoDetail.as_view()),
    path('categorie/', CategoriaList.as_view()),
    path('categorie/<int:id>/', CategoriaDetail.as_view()),

    path('auth/register/', RegisterView.as_view()),
    path('auth/me/', MeView.as_view()),
]