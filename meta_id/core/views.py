from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import EnteSerializer, ClassificacaoSerializer
from .models import ClassificacaoArtistica


class EnteListView(APIView):

    def get(self, *args):
        return Response(status=200)

    def post(self, request):
        serializer = EnteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassificacoesListView(APIView):
    def get(self, *args):
        classificacoes = ClassificacaoArtistica.objects.all()
        serializer = ClassificacaoSerializer(classificacoes, many=True)
        return Response(serializer.data)
