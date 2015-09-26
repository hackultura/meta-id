from rest_framework.views import APIView
from rest_framework.response import Response

class EnteListView(APIView):

    def get(self, *args):
        return Response(status=200)

