from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    EnteSerializer,
    ClassificacaoSerializer,
    PerfilArtisticoSerializer,
    generate_atuacao_json
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


class EnteDetailView(APIView):
    def get(self, request, slug):
        ente = Ente.objects.get(slug=slug)
        serializer = EnteSerializer(ente, context={'request': request})
        return Response(serializer.data)

    def put(self, request, slug):
        ente = Ente.objects.get(slug=slug)
        serializer = EnteSerializer(ente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassificacoesListView(APIView):
    def get(self, request):
        classificacoes = ClassificacaoArtistica.objects.all()
        serializer = ClassificacaoSerializer(classificacoes, many=True)
        return Response(serializer.data)


class AtuacoesListView(APIView):
    def get(self, request):
        return Response(generate_atuacao_json())


class PerfilArtisticoView(APIView):
    def get(self, request, slug):
        ente = Ente.objects.get(slug=slug)
        perfis = PerfilArtistico.objects.filter(ente=ente)
        serializer = PerfilArtisticoSerializer(perfis, many=True)
        return Response(serializer.data)

    def post(self, request, slug):
        ente = Ente.objects.get(slug=slug)
        serializer = PerfilArtisticoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ente=ente)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerfilArtisticoDetailView(APIView):
    def get(self, request, slug):
        perfil = PerfilArtistico.objects.get(slug=slug)
        serializer = PerfilArtisticoSerializer(perfil)
        return Response(serializer.data)

    def put(self, request, slug):
        perfil = PerfilArtistico.objects.get(slug=slug)
        serializer = PerfilArtisticoSerializer(perfil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


