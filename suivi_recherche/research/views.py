from rest_framework import viewsets
from .models import Research, Researcher, Publication
from .serializers import ResearchSerializer, ResearcherSerializer, PublicationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class ResearchViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Research.objects.all()
    serializer_class = ResearchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'start_date', 'researcher']

class ResearcherViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'specialty', 'research']

class PublicationViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'publication_date', 'research']
