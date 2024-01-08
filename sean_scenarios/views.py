from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from sean_scenarios.models import SeanScenarios, Situations, Tags, Interest
from sean_scenarios.serializers import SeanScenariosSerializer, SituationsSerializer, TagsSerializer, InterestSerializer


class SituationsViewSet(ViewSet):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Situations, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Situations.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = SituationsSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'List of Situations',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        situation = self.get_object(pk)
        serializer = SituationsSerializer(situation)
        response = {
            'status': "success",
            'message': 'Situation details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            "situation": request.data.get("situation"),
        }
        
        serializer = SituationsSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Situations created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': "failed",
            'message': 'Situations creation failed',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        situation = self.get_object(pk)
        
        request_data = {
            "situation": request.data.get("situation", situation.situation),
        }
        
        serializer = SituationsSerializer(situation, data=request_data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Situations updated successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        
        response = {
            'status': "failed",
            'message': 'Situations update failed',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        situation = self.get_object(pk)
        situation.delete()
        response = {
            'status': "success",
            'message': 'Situations deleted successfully',
        }
        return Response(response, status=status.HTTP_200_OK)

class InterestViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Interest, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Interest.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = InterestSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'List of Interest',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        interest = self.get_object(pk)
        serializer = InterestSerializer(interest)
        response = {
            'status': "success",
            'message': 'Interest details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            "interest": request.data.get("interest"),
        }
        
        serializer = InterestSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Interest created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': "failed",
            'message': 'Interest creation failed',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        interest = self.get_object(pk)
        
        request_data = {
            "interest": request.data.get("interest", interest.interest),
        }
        
        serializer = InterestSerializer(interest, data=request_data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Interest updated successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        
        response = {
            'status': "failed",
            'message': 'Interest update failed',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        interest = self.get_object(pk)
        interest.delete()
        response = {
            'status': "success",
            'message': 'Interest deleted successfully',
        }
        return Response(response, status=status.HTTP_200_OK)

class TagsViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(Tags, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Tags.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = TagsSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'List of Tags',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        tag = self.get_object(pk)
        serializer = TagsSerializer(tag)
        response = {
            'status': "success",
            'message': 'Tag details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            "tag": request.data.get("tag"),
        }
        
        serializer = TagsSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Tags created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': "failed",
            'message': 'Tags creation failed',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        tag = self.get_object(pk)
        
        request_data = {
            "tag": request.data.get("tag", tag.tag),
        }
        
        serializer = TagsSerializer(tag, data=request_data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'Tags updated successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        
        response = {
            'status': "failed",
            'message': 'Tags update failed',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        tag = self.get_object(pk)
        tag.delete()
        response = {
            'status': "success",
            'message': 'Tags deleted successfully',
        }
        return Response(response, status=status.HTTP_200_OK)

class SeanScenariosViewSet(ViewSet):
    @staticmethod
    def get_object(pk=None):
        return get_object_or_404(SeanScenarios, pk=pk)
    
    @staticmethod
    def get_queryset():
        return SeanScenarios.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = SeanScenariosSerializer(queryset, many=True)
        response = {
            'status': "success",
            'message': 'List of SeanScenarios',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        sean_scenario = self.get_object(pk)
        serializer = SeanScenariosSerializer(sean_scenario)
        response = {
            'status': "success",
            'message': 'SeanScenarios details',
            'data': serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        request_data = {
            "scenario": request.data.get("scenario"),
            "thumbnail": request.data.get("thumbnail"),
            "level": request.data.get("level"),
            "competency": request.data.get("competency", "").split(",") if request.data.get("competency") else []
        }
        
        request_data['competency'] = [int(id) for id in request_data['competency'] if id.isdigit()]
        
        situations = request.data.get('situations', [])
        interests = request.data.get('interests', [])
        tags = request.data.get('tags', [])
        
        if isinstance(situations, str):
            situations = [int(situation) for situation in situations.split(',')]
        if isinstance(interests, str):
            interests = [int(interest) for interest in interests.split(',')]
        if isinstance(tags, str):
            tags = [int(tag) for tag in tags.split(',')]
        
        context = {
            'situations_ids': situations,
            'interest_ids': interests,
            'tags_ids' : tags
        }
        
        serializer = SeanScenariosSerializer(data=request_data, context=context)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'SeanScenarios created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            'status': "failed",
            'message': 'SeanScenarios creation failed',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        sean_scenario = self.get_object(pk)
        
        request_data = {
            "scenario": request.data.get("scenario", sean_scenario.scenario),
            "thumbnail": request.data.get("thumbnail", sean_scenario.thumbnail),
            "level": request.data.get("level", sean_scenario.level),
            "competency": request.data.get("competency", sean_scenario.competency).split(",") if request.data.get("competency") else []
        }
        
        request_data['competency'] = [int(id) for id in request_data['competency'] if id.isdigit()]
        
        situations = request.data.get('situations', [])
        interests = request.data.get('interests', [])
        tags = request.data.get('tags', [])
        
        if isinstance(situations, str):
            situations = [int(situation) for situation in situations.split(',')]
        if isinstance(interests, str):
            interests = [int(interest) for interest in interests.split(',')]
        if isinstance(tags, str):
            tags = [int(tag) for tag in tags.split(',')]
        
        context = {
            'situations_ids': situations,
            'interest_ids': interests,
            'tags_ids' : tags
        }
        
        serializer = SeanScenariosSerializer(sean_scenario, data=request_data, context=context, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': "success",
                'message': 'SeanScenarios updated successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        
        response = {
            'status': "failed",
            'message': 'SeanScenarios update failed',
            'data': serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        sean_scenario = self.get_object(pk)
        sean_scenario.delete()
        response = {
            'status': "success",
            'message': 'SeanScenarios deleted successfully',
        }
        return Response(response, status=status.HTTP_200_OK)

