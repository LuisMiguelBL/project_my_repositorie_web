from django.contrib import admin
from .models import Tarefa
# Register your models here.

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'concluida', 'criado_em']

    list_filter = ['concluida']

    search_fields = ['titulo', 'descricao']