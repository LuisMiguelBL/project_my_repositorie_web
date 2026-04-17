from django.db import models

class Projeto(models.Model):
    TIPO_CHOICES = [
        ('PESSOAL', 'Pessoal'),
        ('DISCIPLINA', 'Disciplina'),
    ]

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    link_git = models.URLField()

    def __str__(self):
        return self.nome


class Certificado(models.Model):
    descricao = models.TextField()


# Create your models here.
