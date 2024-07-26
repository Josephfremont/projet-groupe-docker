from rest_framework import serializers
from .models import Research, Researcher, Publication

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = '__all__'

class ResearcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Researcher
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
