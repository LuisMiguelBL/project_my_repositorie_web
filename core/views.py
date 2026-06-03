from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Pessoa
from .serializers import PessoaSerializer




def home(request):

        return render(request, 'portfolio/home.html')


class PerfilDetail(generics.RetrieveUpdateAPIView):
    """
    GET   /api/perfil/ → Retorna o perfil do usuario logado
    PUT   /api/perfil/ → Atualiza o perfil completo
    PATCH /api/perfil/ → Atualiza parcialmente
    """

    serializer_class = PessoaSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):

        perfil, created = Pessoa.objects.get_or_create(
            usuario=self.request.user,
            defaults={'nome': self.request.user.username},
        )
        return perfil