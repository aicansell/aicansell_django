from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Words
from .serializers import WordSerializer
from rest_framework import generics, status  

from rest_framework.viewsets import ViewSet
from rest_framework_tracking.mixins import LoggingMixin


      
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


class WordsViewSet(LoggingMixin, ViewSet):
    serializer_class = WordSerializer

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Org, id=pk)


    @staticmethod
    def get_queryset():
        return Org.objects.all()


    def list(self, request):
        serialized_data = self.serializer_class(self.get_queryset(), many=True).data
        response = {
            'status': 'Success',
            'data': serialized_data,
        }
        return Response(response, status=status.HTTP_200_OK)


    def retrieve(self, request, **kwargs):
        pk = kwargs.pop('pk')
        response = {
            'status': 'Success',
            'data': self.serializer_class(self.get_object(pk)).data
        }
        return Response(response, status=status.HTTP_200_OK)


    def create(self, request):
        request_data = self.request.data
        data = {
            'word_name': request_data.get('word_name'),
        }

        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'word was successfully created.'
        }
        return Response(response, status=status.HTTP_201_CREATED)


    def update(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        request_data = self.request.data

        data = {
            'word_name': request_data.get('word_name', instance.word_name),
        }

        serialized_data = self.serializer_class(instance=instance, data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        response = {
            'status': 'Success',
            'data': serialized_data.data,
            'message': 'word was successfully updated.'
        }
        return Response(response, status=status.HTTP_200_OK)


    def destroy(self, request, **kwargs):
        instance = self.get_object(kwargs.pop('pk'))
        instance.delete()

        response = {
            'data': '',
            'message': "Successfully deleted word"
        }

        return Response(response, status=status.HTTP_204_NO_CONTENT)                