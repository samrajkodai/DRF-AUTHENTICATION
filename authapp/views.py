from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import generics
from rest_framework import mixins

class TransformerList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):


        def get(self, request, format=None):
           
            return Response({"serializer.data"})
