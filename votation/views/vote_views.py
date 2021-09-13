from votation.models import Vote
from votation.serializers import VoteCreateUpdateSerializer, VoteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class VoteList(APIView):
    def get(self, request, format=None):
        vote_list = Vote.objects.all()
        serializer = VoteSerializer(vote_list, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        voter_ip = self.__get_voter_ip(request)
        if voter_ip:
            ip_update = {'ip': voter_ip}
            request.data.update(ip_update)
   
        serializer = VoteCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def __get_voter_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
