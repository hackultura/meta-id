# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from .serializers import (
    EnteSerializer,
    ClassificacaoSerializer,
    PerfilArtisticoSerializer,
    DocumentoSerializer,
    generate_atuacao_json,
    create_serializer_portfolio_type
)
from .models import (
    Ente,
    ClassificacaoArtistica,
    PerfilArtistico,
    Documento,
    get_portfolio_or_404
)


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
        ente = get_object_or_404(Ente, user__slug=slug)
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
        ente = get_object_or_404(Ente, user__slug=slug)
        perfis = PerfilArtistico.objects.filter(ente=ente)
        serializer = PerfilArtisticoSerializer(perfis, many=True,
                                               context={'request': request})
        return Response(serializer.data)

    def post(self, request, slug):
        ente = get_object_or_404(Ente, user__slug=slug)
        serializer = PerfilArtisticoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ente=ente)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerfilArtisticoDetailView(APIView):
    def get(self, request, slug):
        perfil = get_object_or_404(PerfilArtistico, slug=slug)
        serializer = PerfilArtisticoSerializer(perfil,
                                               context={'request': request})
        return Response(serializer.data)

    def put(self, request, slug):
        perfil = get_object_or_404(PerfilArtistico, slug=slug)
        serializer = PerfilArtisticoSerializer(perfil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        perfil = get_object_or_404(PerfilArtistico, slug=slug)
        perfil.delete()
        return Response(status=status.HTTP_200_OK)


class PortfolioView(APIView):
    parser_classes = (MultiPartParser, FormParser, JSONParser,)

    def post(self, request, type, slug):
        perfil = get_object_or_404(PerfilArtistico, slug=slug)
        request.data['perfil'] = perfil.pk
        serializer = create_serializer_portfolio_type(
            type, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PortfolioDetailView(APIView):
    def get(self, request, slug, type, uid):
        portfolio = get_portfolio_or_404(type=type, uid=uid)
        serializer = create_serializer_portfolio_type(type, portfolio)
        return Response(serializer.data)

    def delete(self, request, slug, type, uid):
        portfolio = get_portfolio_or_404(type=type, uid=uid)
        portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DocumentoView(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        serializer = DocumentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentoDetailView(APIView):
    def delete(self, request, uid):
        instance = Documento.objects.get(id_pub=uid)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
