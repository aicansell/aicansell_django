from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Words
from .serializers import WordSerializer
from rest_framework import generics, status  


      
class ProductView(generics.ListCreateAPIView):  
        queryset = Words.objects.all()  
        serializer_class = WordSerializer
      
        def create(self, request, *args, **kwargs):  
            serializer = self.get_serializer(data=request.data, many=True)  
            serializer.is_valid(raise_exception=True)  
      
            try:  
                self.perform_create(serializer)  
                return Response(serializer.data, status=status.HTTP_201_CREATED)  
            except:  
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        