#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sub_Competency
from .serializers import Sub_CompetencySerializer
from rest_framework import generics, status  


      
class ProductView(generics.ListCreateAPIView):  
        queryset = Sub_Competency.objects.all()  
        serializer_class = Sub_CompetencySerializer
      
        def create(self, request, *args, **kwargs):  
            serializer = self.get_serializer(data=request.data, many=True)  
            serializer.is_valid(raise_exception=True)  
      
            try:  
                self.perform_create(serializer)  
                return Response(serializer.data, status=status.HTTP_201_CREATED)  
            except:  
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        