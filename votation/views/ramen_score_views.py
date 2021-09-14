from votation.models import RamenScore
from votation.serializers import (
    RamenScoreSerializer, 
    RamenScoreCreateUpdateSerializer,
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RamenScoreList(APIView):
    def get(self, request, format=None):
        score_list = RamenScore.objects.all()
        serializer = RamenScoreSerializer(score_list, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = RamenScoreCreateUpdateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
