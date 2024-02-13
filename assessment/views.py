from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import pagination
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from assessment.models import Situation, Style
from assessment.models import Assessment1, Assessment2, Assessment3
from assessment.models import Assessment, AssessmentResult
from assessment.serializers import Assessment1Serializer, Assessment2Serializer, Assessment3Serializer

from datetime import datetime

import threading

class AssessmentPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

class Assessment1ViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    
    pagination_class = AssessmentPagination
    
    @staticmethod
    def get_queryset():
        return Assessment1.objects.all()
    
    def list(self, request):
        user = request.user
        date_joined = user.date_joined
        days_since_joined = (datetime.now() - date_joined).days
        analytics_instance = AssessmentResult.objects.filter(user=user)
        
        access = ""
        flag= False
        
        if days_since_joined <= 29:
            access = "pre"
            instance = analytics_instance.get(access=access)
            if not instance:
                flag= True
            else:
                flag= False
        elif days_since_joined >= 30 and days_since_joined <= 59:
            access = "mid"
            instance = analytics_instance.get(access=access)
            if not instance:
                flag= True
            else:
                flag= False
        elif days_since_joined >= 60:
            access = "post"
            instance = analytics_instance.get(access=access)
            if not instance:
                flag= True
            else:
                flag= False
        
        if not flag:
            response = {
                'status': 'success',
                'message': f'Sorry, you have already taken the {access} assessment',
            }
            return Response(response, status=status.HTTP_200_OK)
        
        queryset = self.get_queryset(access__icontains=access)
        
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        serializer = Assessment1Serializer(paginated_queryset, many=True)
        
        response =  paginator.get_paginated_response(serializer.data)
        
        response_data = {
            'status': 'success',
            'message': 'Assessment1 list',
            'access': access,
            'data': response.data
        }

        return Response(response_data, status=status.HTTP_200_OK)

class Assessment1ProcessingViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return Assessment1.objects.all()
    
    def list(self, request):
        def updating_assessmentresult_score(request, access, result):
            assessment_instance = Assessment.objects.get(name__icontains="assessment1")
            if assessment_instance:
                obj = AssessmentResult.objects.create(user=request.user, assessment=assessment_instance.id,
                                                    phase=access, result=result)
                obj.save()
            else:
                print("Assessment not found")
        
        ids = request.query_params.get('ids', [])
        access = request.query_params.get('access')
        
        instance = AssessmentResult.objects.get(user=request.user, access=access)
        
        if instance:
            response = {
                'status': 'success',
                'message': f'Sorry, you have already taken the {access} assessment',
            }
            return Response(response, status=status.HTTP_200_OK)
        
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
        
        processing_thread = threading.Thread(
            target=updating_assessmentresult_score,
            args=(request, access, result)
        )
        processing_thread.start()

        response = {
            'status': 'success',
            'message': 'Assessment1 processing list',
            'data': result
        }
        return Response(response, status=status.HTTP_200_OK)

class Assessment2ViewSet(ViewSet):
    pagination_class = AssessmentPagination
    
    @staticmethod
    def get_queryset():
        return Assessment2.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        serializer = Assessment2Serializer(paginated_queryset, many=True)
        
        response =  paginator.get_paginated_response(serializer.data)
        
        response_data = {
            'status': 'success',
            'message': 'Assessment2 list',
            'data': response.data
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
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
    pagination_class = AssessmentPagination
    
    @staticmethod
    def get_queryset():
        return Assessment3.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        serializer = Assessment3Serializer(paginated_queryset, many=True)
        
        response =  paginator.get_paginated_response(serializer.data)
        
        response_data = {
            'status': 'success',
            'message': 'Assessment3 list',
            'data': response.data
        }

        return Response(response_data, status=status.HTTP_200_OK)

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
            result = "You have severely low self-esteem"
        else:
            result = "Sorry, Unable to find, please try again."
            
        response = {
            'status': 'success',
            'message': 'Assessment3 processing list',
            'data': result
        }
        
        return Response(response, status=status.HTTP_200_OK)
