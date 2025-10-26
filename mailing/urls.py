from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubscriptionViewSet, NotificationViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('subscriptions', SubscriptionViewSet, basename='subscription')
router.register('notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]
