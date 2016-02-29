from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AnaliseEnteSerializer


class AnaliseDetailView(APIView):

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

    def get(self, request, slug, format='json'):
        return Response(status.HTTP_200_OK)

    def post(self, request, slug, format='json'):
        serializer = AnaliseEnteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
