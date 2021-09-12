from votation.models import RamenYa
from votation.serializers import RamenYaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RamenYaList(APIView):
    """
    List all ramen restaurants, or create a new one.
    """
    def get(self, request, format=None):
        ramenya_list = RamenYa.objects.all()
        serializer = RamenYaSerializer(ramenya_list, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RamenYaSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
