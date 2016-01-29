from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AnaliseEnteView(APIView):

    """
        AnaliseEnteView return data for a especific analyse for a given ente.
    """

    def __init__(self):
        """TODO: to be defined1. """
    def get(self, request, format='json'):
        return Response(status.HTTP_200_OK)


class AnaliseListView(APIView):

    """
        AnaliseEnteView return data for a especific analyse for a given ente.
    """

    def __init__(self):
        """TODO: to be defined1. """
    def get(self, request, slug, format='json'):
        return Response(status.HTTP_200_OK)
