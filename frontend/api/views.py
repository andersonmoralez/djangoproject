from rest_framework.views import APIView
from .models import EventRegister
from .serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.shortcuts import render

class RegisterListView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = RegisterSerializer
    
    def get(self, request, format=None):
        registers = EventRegister.objects.all()
        serializer = RegisterSerializer(registers, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"messagem": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def get(self, request, pk):
        register = EventRegister.objects.get(pk=pk)
        serializer = self.serializer_class(register)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        register = EventRegister.objects.get(pk=pk)
        serializer = self.serializer_class(register, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            register = EventRegister.objects.get(pk=pk)
            register.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(status=status.HTTP_404_NOT_FOUND)

def render_registers(request):
    registers = EventRegister.objects.all()
    return render(request, 'api/index.html', {'registers': registers})