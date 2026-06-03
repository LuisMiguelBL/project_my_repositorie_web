from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            'id','nome','descricao','curso','periodo',
            'email','git','linked','url_imagem'
        ]