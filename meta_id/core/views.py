from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    EnteSerializer,
    ClassificacaoSerializer,
    PerfilArtisticoSerializer
)
from .models import Ente, ClassificacaoArtistica, PerfilArtistico


class EnteView(APIView):

    def get(self, *args):
        entes = Ente.objects.all()
        serializer = EnteSerializer(entes, many=True)
        return Response(serializer.data)

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


class PerfilArtisticoView(APIView):
    def get(self, request, uid):
        ente = Ente.objects.get(id_pub=uid)
        perfis = PerfilArtistico.objects.filter(ente=ente)
        serializer = PerfilArtisticoSerializer(perfis, many=True)
        return Response(serializer.data)

    def post(self, request, uid):
        ente = Ente.objects.get(id_pub=uid)
        serializer = PerfilArtisticoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ente=ente)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


