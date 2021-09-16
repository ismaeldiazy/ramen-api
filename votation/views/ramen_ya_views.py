from votation.models import RamenYa
from votation.serializers import RamenYaSerializer, RamenYaCreateUpdateSerializer
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
        serializer = RamenYaCreateUpdateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RamenYaDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return RamenYa.objects.get(pk=pk)
        except RamenYa.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        ramen = self.get_object(pk)
        serializer = RamenYaSerializer(ramen)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        ramen = self.get_object(pk=pk)
        ramen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, format=None):
        ramen = self.get_object(pk=pk)
        serializer = RamenYaCreateUpdateSerializer(ramen, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
