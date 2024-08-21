from django.urls import path
from .views import TestList, BolimList, BolimDetail

urlpatterns = [
    path('tests/', TestList.as_view(), name='test-list'),
    path('bolim/', BolimList.as_view(), name='bolim-list'),
    path('api/bolims/<int:pk>/', BolimDetail.as_view(), name='bolim-detail-api'),

]
