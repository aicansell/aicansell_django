from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import pagination
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from SaaS.permissions import SaaSAccessPermissionAssessment
from assessments.models import Question, Option, AssessmentType
from assessments.models import Assessment, AssessmentResult
from assessments.serializers import QuestionSerializer, OptionSerializer, OptionListSerializer
from assessments.serializers import AssessmentSerializer, AssessmentResultSerializer, AssessmentTypeSerializer

from datetime import datetime

import threading

class QuestionViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    
    @staticmethod
    def get_queryset():
        return Question.objects.all()
    
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Question, pk=pk)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionSerializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'Questions list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = QuestionSerializer(instance)
        response = {
            'status': 'success',
            'message': 'Question details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Question created',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = QuestionSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Question updated',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': 'success',
            'message': 'Question deleted',
            'data': None
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class OptionViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return Option.objects.all()
    
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Option, pk=pk)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = OptionListSerializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'Options list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = OptionListSerializer(instance)
        response = {
            'status': 'success',
            'message': 'Option details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Option created',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = OptionSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Option updated',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': 'success',
            'message': 'Option deleted',
            'data': None
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class AssessmentTypeViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return AssessmentType.objects.all()
    
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(AssessmentType, pk=pk)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = AssessmentTypeSerializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'Assessment types list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = AssessmentTypeSerializer(instance)
        response = {
            'status': 'success',
            'message': 'Assessment type details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = AssessmentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Assessment type created',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = AssessmentTypeSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Assessment type updated',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': 'success',
            'message': 'Assessment type deleted',
            'data': None
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class AssessmentViewSet(ViewSet):
    @staticmethod
    def get_queryset():
        return Assessment.objects.all()
    
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Assessment, pk=pk)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = AssessmentSerializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'Assessments list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = AssessmentSerializer(instance)
        response = {
            'status': 'success',
            'message': 'Assessment details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Assessment created',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = AssessmentSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Assessment updated',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': 'success',
            'message': 'Assessment deleted',
            'data': None
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class AssessmentResultViewSet(ViewSet):
    permission_classes = [IsAuthenticated, SaaSAccessPermissionAssessment]
    
    @staticmethod
    def get_queryset():
        return AssessmentResult.objects.all()
    
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(AssessmentResult, pk=pk)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = AssessmentResultSerializer(queryset, many=True)
        response = {
            'status': 'success',
            'message': 'Assessment results list',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = AssessmentResultSerializer(instance)
        response = {
            'status': 'success',
            'message': 'Assessment result details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = AssessmentResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Assessment result created',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = AssessmentResultSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'message': 'Assessment result updated',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        response = {
            'status': 'error',
            'message': 'Invalid data',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        response = {
            'status': 'success',
            'message': 'Assessment result deleted',
            'data': None
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
