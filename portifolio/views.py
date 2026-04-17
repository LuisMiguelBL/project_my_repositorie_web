from django.shortcuts import render

from portifolio.models import Projeto, Certificado
from core.models import Pessoa


def home(request):
    certificados = Certificado.objects.all()
    pessoa = Pessoa.objects.first()
    return render(request,'portifolio/home.html', {'certificados':certificados, 'pessoa':pessoa} )

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request,'portifolio/projetos.html',{'projetos':projetos})

def contato(request):
    pessoa = Pessoa.objects.first()
    return render(request,'portifolio/contato.html',{'pessoa':pessoa})
# Create your views here.
