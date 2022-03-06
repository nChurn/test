from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.emotitoken_serializer import EmotitokenSerializer
from .logic import get_emotitoken

from django.conf import settings
#from .logic import CreateEmotitokenLogic

# Create your views here.

class GetEmotitokenView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmotitokenSerializer

    def get(self, request):
        description = request.query_params.get('description', None)
        if not description:
            raise ValueError("Description must be set")

        width = request.query_params.get('width', None)
        try:
            width = int(width)
        except:
            return Response("Width must be number", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        height = request.query_params.get('height', None)
        try:
            height = int(height)
        except:
            return Response("Height must be number", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
        emotitoken = get_emotitoken(description, width, height)

        return Response(emotitoken, content_type='image/png')