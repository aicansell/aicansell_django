from rest_framework import serializers

from sean_scenarios.models import SeanScenarios, Situations, Interest, Tags
from sean_scenarios.models import SeanScenariosSituations, SeanScenariosInterests, SeanScenariosTags

class SituationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situations
        fields = ['id', 'situation']
        
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['id', 'interest']
        
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'tag']
        
class SeanScenariosSerializer(serializers.ModelSerializer):
    competency = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = SeanScenarios
        fields = ['id', 'scenario', 'thumbnail', 'level', 'competency']
        
    def save(self, *args, **kwargs):
        seanscenarios = super().save()
        situations_ids = self.context.get('situations_ids')
        interest_ids = self.context.get('interest_ids')
        tags_ids = self.context.get('tags_ids')
        
        if situations_ids:
            situations = Situations.objects.filter(id__in=situations_ids)
            seanscenarios_situation = [
                SeanScenariosSituations(scenario=seanscenarios, situation=situation)
                for situation in situations
            ]
            SeanScenariosSituations.objects.bulk_create(seanscenarios_situation)
            
        if interest_ids:
            interests = Interest.objects.filter(id__in=interest_ids)
            seanscenarios_interest = [
                SeanScenariosInterests(scenario=seanscenarios, interest=interest)
                for interest in interests
            ]
            SeanScenariosInterests.objects.bulk_create(seanscenarios_interest)
            
        if tags_ids:
            tags = Tags.objects.filter(id__in=tags_ids)
            seanscenarios_tags = [
                SeanScenariosTags(scenario=seanscenarios, tag=tag)
                for tag in tags
            ]
            SeanScenariosTags.objects.bulk_create(seanscenarios_tags)
            
        return seanscenarios
