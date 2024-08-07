from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet, BolimViewSet, UserTestAttemptViewSet

router = DefaultRouter()

router.register(r'bolim', BolimViewSet)
router.register(r'user-test-attempts', UserTestAttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tests/', TestViewSet.as_view(), ),
]