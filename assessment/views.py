from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from assessment.models import Situation, Style
from assessment.models import Assessment1, Assessment2, Assessment3
from assessment.serializers import Assessment1Serializer, Assessment2Serializer, Assessment3Serializer

class Assessment1ViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return Assessment1.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = Assessment1Serializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'Assessment1 list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

class Assessment1ProcessingViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return Assessment1.objects.all()
    
    def list(self, request):
        ids = request.query_params.get('ids', [])
        
        if isinstance(ids, str):
            ids = [int(id) for id in ids.split(',')]
        
        res, result  = {}, {}
            
        for id in ids:
            instance = Situation.objects.get(id=id)
            res[str(instance.style.name)] = 1 + res.get(str(instance.style.name), 0)
            
        if len(res)>0:
            max_situation = max(res, key=lambda k: res[k])
            result['max_situation'] = max_situation
        
        result['situations'] = res

        response = {
            'status': 'success',
            'message': 'Assessment1 processing list',
            'data': result
        }
        return Response(response, status=status.HTTP_200_OK)

class Assessment2ViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return Assessment2.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = Assessment2Serializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'Assessment2 list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
class Assessment2ProcessingViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return Assessment2.objects.all()
    
    def list(self, request):
        ids = self.request.query_params.get('ids', [])
        
        if isinstance(ids, str):
            ids = [int(id) for id in ids.split(',')]
        
        res, result = {}, {}
        
        for id in ids:
            instance = Situation.objects.get(id=id)
            res[str(instance.style.name)] = 1 + res.get(str(instance.style.name), 0)
        
        if len(res)>0:
            max_situation = max(res, key=lambda k: res[k])
            msg = Style.objects.filter(name__icontains=max_situation).first()
            result['max_situation'] = max_situation
            result['message'] = msg.msg
            
        result['situations'] = res
        
        response = {
            'status': 'success',
            'message': 'Assessment2 processing list',
            'data': result
        }
        return Response(response, status=status.HTTP_200_OK)
    
class Assessment3ViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return Assessment3.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = Assessment3Serializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'Assessment3 list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

class Assessment3ProcessingViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return Assessment3.objects.all()
    
    def list(self, request):
        ids = self.request.query_params.get('ids', [])
        
        if isinstance(ids, str):
            ids = [int(id) for id in ids.split(',')]
            
        if len(ids)>=0 and len(ids)<=4:
            result = "You have failry good self-esteem"
        elif len(ids)>=5 and len(ids)<=10:
            result = "You have mild low self-esteem"
        elif len(ids)>=11 and len(ids)<=18:
            result = "You have moderately low self-esteem"
        elif len(ids)>=19 and len(ids)<=50:
            resukt = "You have severely low self-esteem"
        else:
            result = "Sorry, Unable to find, please try again."
            
        response = {
            'status': 'success',
            'message': 'Assessment3 processing list',
            'data': result
        }
        
        return Response(response, status=status.HTTP_200_OK)
