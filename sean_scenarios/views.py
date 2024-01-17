from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from accounts.models import UserProfile
from sean_scenarios.models import SeanScenarios, Situations, Tags, Interest
from sean_scenarios.models import SeanScenariosInterests, SeanScenariosSituations, SeanScenariosTags
from sean_scenarios.serializers import SeanScenariosSerializer, SituationsSerializer, TagsSerializer, InterestSerializer

from django.conf import settings
from pathlib import Path
from sean_scenarios.cron import send_monthly_email

import json
import threading
import pandas as pd

class SituationsViewSet(ViewSet):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Situations, pk=pk)
    
    @staticmethod
    def get_queryset():
        return Situations.objects.all()
    
    def list(self, request):
        situation = request.query_params.get('situation')
        queryset = self.get_queryset()
        if situation:
            queryset = queryset.filter(situation__icontains=situation)
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
        interest = request.query_params.get('interest')
        queryset = self.get_queryset()
        if interest:
            queryset = queryset.filter(interest__icontains=interest)
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
        send_monthly_email()
        tag = request.query_params.get('tag')
        queryset = self.get_queryset()
        if tag:
            queryset = queryset.filter(tag__icontains=tag)
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
        situation, interest = request.query_params.get('situation'), request.query_params.get('interest')
        tag = request.query_params.get('tag')
        queryset = self.get_queryset()
        
        if situation or interest or tag:
            if situation:
                data = SeanScenariosSituations.objects.filter(situation__situation__icontains=situation)
                queryset = [obj.scenario for obj in data]
            if interest:
                data = SeanScenariosInterests.objects.filter(interest__interest__icontains=interest)
                queryset = [obj.scenario for obj in data]
            if tag:
                data = SeanScenariosTags.objects.filter(tag__tag__icontains=tag)
                queryset = [obj.scenario for obj in data]
        
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

class SeanScenarioProcessingViewSet(ViewSet):
    def list(self, request):
        def process_user_data(request, user_power_words, user_weak_words, score, competencys, scenario_answer):
            print("\n\nStarting Thread: UserProfile")
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)
                if user_profile:
                    user_profile.scenarios_attempted += 1
                    user_profile.user_powerwords = (user_profile.user_powerwords or '') + "," + ", ".join(user_power_words)
                    user_profile.user_weakwords = (user_profile.user_weakwords or '') + "," + ", ".join(user_weak_words)
                    user_profile.user_powerwords = user_profile.user_powerwords.strip(',')
                    user_profile.user_weakwords = user_profile.user_weakwords.strip(',')
                    if user_profile.scenarios_attempted_score:
                        user_profile.scenarios_attempted_score += str(score) + ','
                    else:
                        user_profile.scenarios_attempted_score = str(score) + ','
                    print("\n\nCompleted Thread: UserProfile")
                    print("\n\nStarting Thread: Update Competency")
                    try:
                        competency_score = json.loads(user_profile.competency_score)
                    except:
                        competency_score = {}

                    for competency in competencys:
                        sub_competencies = competency.sub_competency.all()
                        power_word_list = []
                        negative_word_list = []

                        for sub_competency in sub_competencies:
                            power_words = sub_competency.power_words.all()
                            negative_words = sub_competency.negative_words.all()

                            for power_word in power_words:
                                power_word_list.append(power_word.word.word_name.lower())

                            for negative_word in negative_words:
                                negative_word_list.append(negative_word.word.word_name.lower())

                        power_word_count = 0
                        negative_word_count = 0
                        
                        power_word_count = sum(1 for word in power_word_list if word in scenario_answer)
                        negative_word_count = sum(1 for word in negative_word_list if word in scenario_answer)

                        
                        competency_name = str(competency.competency_name)
                                
                        if competency_name in competency_score:
                            competency_score[competency_name] += ',' + str(power_word_count - negative_word_count)
                            competency_score[competency_name] = competency_score[competency_name]
                        else:
                            competency_score[competency_name] = str(power_word_count - negative_word_count)

                    user_profile.competency_score = json.dumps(competency_score)
                    user_profile.save()
                    print("\n\nCompleted Thread: Update Competency")
            else:
                print("\n\nUser not authenticated")
                print("\n\nCompleted Thread: Update Competency")         

        def words_update(request, words):
            print("Starting words update")
            words = scenario_answer.split()

            df = pd.DataFrame(words, columns=['Words'])
            excel_file_path = Path('Word_Data.xlsx')
            
            if excel_file_path.exists():
                existing_df = pd.read_excel(excel_file_path)
                unique_words = set(existing_df['Words'])
                new_words = [word for word in words if word not in unique_words]
                new_df = pd.DataFrame(new_words, columns=['Words'])
                df = pd.concat([existing_df, new_df], ignore_index=True)
            df.to_excel(excel_file_path, index=False)
            print("Successfully updated words")

        try:
            instance = SeanScenarios.objects.get(id=request.query_params.get('id'))
        except:
            response = {
                'status': "failed",
                'message': 'SeanScenarios does not exist',
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        scenario_answer = request.query_params.get('scenario_answer').lower()
        
        processing_thread = threading.Thread(
            target=words_update,
            args=(request, scenario_answer)
        )
        processing_thread.start()
        
        
        competencys = instance.competency.all().prefetch_related(
            'sub_competency__power_words__word',
            'sub_competency__negative_words__word',
        )
        
        power_word_list = []
        negative_word_list = []
        
        for competency in competencys:
            sub_competencies = competency.sub_competency.all()
            for sub_competency in sub_competencies:
                power_words = sub_competency.power_words.all()
                for power_word in power_words:
                    power_word_list.append(power_word.word.word_name.lower())
                negative_words = sub_competency.negative_words.all()
                for negative_word in negative_words:
                    negative_word_list.append(negative_word.word.word_name.lower())
                    
        user_scenario_answer = scenario_answer
        
        instance.scenario_answer = instance.scenario_answer + " " + scenario_answer
        
        user_power_words = []
        user_weak_words = []
        
        for words in power_word_list:
            if words in scenario_answer:
                user_power_words.append(words)
        for words in negative_word_list:
            if words in scenario_answer:
                user_weak_words.append(words)
                
        score = len(user_power_words) - len(user_weak_words)
        
        instance.scenario_answer_count += 1
        
        processing_thread = threading.Thread(
            target=process_user_data,
            args=(request, user_power_words, user_weak_words, score, competencys, user_scenario_answer)
        )
        processing_thread.start()
        
        instance.save()
        
        response = {
            'status': "success",
            'message': 'SeanScenarios processed successfully',
            'data': {
                'compentency_score': score,
                'powerwords_detected': user_power_words,
                'negativewords_detected': user_weak_words,
                'powerwords_list': power_word_list,
                'negativewords_list': negative_word_list,
            }
        }
        
        return Response(response, status=status.HTTP_200_OK)
