from rest_framework import serializers

from icebreaker.models import IceBreaker, IndividualInputScenarios


class IceBreakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceBreaker
        fields = ['id', 'going_for', 'with_who', 'help_on', 'come_across_as', 'not_come_across_as', 'created_by']
        extra_kwargs = {
            'created_by': {'write_only': True}
        }
        

class IndividualInputScenariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualInputScenarios
        fields = ['id', 'need_help_on', 'need_to_talk', 'want_to_say', 'come_across_as', 'not_come_across_as', 'created_by']
        extra_kwargs = {
            'created_by': {'write_only': True}
        }
