from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class PostApiView(APIView):
    def get(self,request):
        return Response(status=status.HTTP_200_OK, data='Hola mi amor que mas pues')