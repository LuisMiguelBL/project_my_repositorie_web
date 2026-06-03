

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework.views import APIView
from rest_framework import generics


# URL: path('v1/', views.tarefa_list_create_fbv)
@api_view(['GET','POST'])
def tarefa_list_create_fbv(request):
    """
        GET  /api/tarefas/v1/ → Lista todas as tarefas
        POST /api/tarefas/v1/ → Cria uma nova tarefa
        """
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def tarefa_detail_fbv(request, pk):
    """
        GET    /api/tarefas/v1/<pk>/ → Retorna uma tarefa especifica
        PUT    /api/tarefas/v1/<pk>/ → Atualiza uma tarefa
        DELETE /api/tarefas/v1/<pk>/ → Exclui uma tarefa
        """

    try:
        tarefa = Tarefa.objects.get(pk=pk)
    except Tarefa.DoesNotExist:
        return Response({'error': "Tarefa não encontrada"},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# ─── Estilo 2: Class-Based Views (APIView) ───

# URL: path('v2/', views.TarefaListCreateAPIView.as_view())

class TarefaListCreateAPIView(APIView):
    """
    GET  /api/tarefas/v2/ → Lista todas as tarefas
    POST /api/tarefas/v2/ → Cria uma nova tarefa
    """

    def get(self, request):                          # GET /api/tarefas/v2/
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)             # ---> JSON lista

    def post(self, request):                         # POST /api/tarefas/v2/
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# URL: path('v2/<int:pk>/', views.TarefaDetailAPIView.as_view())

class TarefaDetailAPIView(APIView):
    """
    GET    /api/tarefas/v2/<pk>/ → Retorna uma tarefa
    PUT    /api/tarefas/v2/<pk>/ → Atualiza uma tarefa
    DELETE /api/tarefas/v2/<pk>/ → Exclui uma tarefa
    """

    def get_object(self, pk):
        try:
            return Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            return None

    def get(self, request, pk):                      # GET /api/tarefas/v2/1/
        tarefa = self.get_object(pk)
        if tarefa is None:
            return Response(
                {'erro': 'Tarefa nao encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk):                      # PUT /api/tarefas/v2/1/
        tarefa = self.get_object(pk)
        if tarefa is None:
            return Response(
                {'erro': 'Tarefa nao encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):                   # DELETE /api/tarefas/v2/1/
        tarefa = self.get_object(pk)
        if tarefa is None:
            return Response(
                {'erro': 'Tarefa nao encontrada'},
                status=status.HTTP_404_NOT_FOUND
            )
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# ─── Estilo 3: Generic Views (RECOMENDADO) ───

# URL: path('v3/', views.TarefaListCreate.as_view())

class TarefaListCreate(generics.ListCreateAPIView):


    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(responsavel=self.request.user)

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)


# URL: path('v3/<int:pk>/', views.TarefaDetail.as_view())

class TarefaDetail(generics.RetrieveUpdateDestroyAPIView):


    Serializer_Class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefa.objects.filter(responsavel=self.request.user)