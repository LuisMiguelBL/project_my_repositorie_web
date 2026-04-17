from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    curso = models.CharField(max_length=100)
    periodo = models.CharField(max_length=20)
    email = models.TextField()
    link_git = models.URLField()
    link_linkedin = models.URLField()
    url= models.URLField()

    def __str__(self):
        return self.nome
# Create your models here.
