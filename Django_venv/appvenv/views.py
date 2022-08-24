from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import Testing

from appvenv.serializers import TestingSerializers

# Create your views here.
@api_view(['GET' , 'POST'])
def testingview(request):
    # obj = testing(text="Hello" , email = "random@gmail.com" , age = "20")
    # obj.save()

    list = Testing.objects.all()
    serializer = TestingSerializers(list,many= True)
    context  = {
        'serializer_class_data':serializer.data
    }
    return Response(serializer.data)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated


# class HelloView(APIView):

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)

class  TestingViewSet(viewsets.ModelViewSet):
    queryset = Testing.objects.all()
    serializer_class = TestingSerializers

