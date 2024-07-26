from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResearchViewSet, ResearcherViewSet, PublicationViewSet

router = DefaultRouter()
router.register(r'research', ResearchViewSet)
router.register(r'researcher', ResearcherViewSet)
router.register(r'publication', PublicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
