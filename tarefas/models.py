from django.conf import settings
from django.db import models


class Tarefa(models.Model):
    """
    Modelo que representa uma tarefa.
    Cada tarefa tem um titulo, descricao, status de conclusao
    e a data em que foi criada.
    """

    # Campo de texto curto (max 200 caracteres) — obrigatorio
    titulo = models.CharField(max_length=200)

    # Campo de texto longo — opcional (blank=True permite vazio no formulario)
    descricao = models.TextField(blank=True)

    # Campo booleano — por padrao, a tarefa nao esta concluida
    concluida = models.BooleanField(default=False)

    # Data e hora automatica — preenchido automaticamente ao criar
    criado_em = models.DateTimeField(auto_now_add=True)

    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tarefas',
        null=True,
        blank=True,
    )

    class Meta:
        # Ordena por data de criacao (mais recente primeiro)
        ordering = ['-criado_em']

    def __str__(self):
        # Representacao em texto da tarefa (aparece no admin)
        return self.titulo