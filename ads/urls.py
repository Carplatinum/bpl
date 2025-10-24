from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdViewSet

router = DefaultRouter()
router.register('', AdViewSet, basename='ads')

urlpatterns = [
    path('', include(router.urls)),
]
