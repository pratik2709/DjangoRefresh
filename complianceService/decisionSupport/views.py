from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Poll
from .serializers import PollSerializer

class PollView(APIView):

    def get(self, request):
        serializer = PollSerializer(Poll.objects.all(), many=True)
        response = {"hello": "world"}
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = PollSerializer(data=data)
        if serializer.is_valid():
            poll = Poll(**data)
            poll.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)