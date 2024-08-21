from django.urls import path
from .views import RegisterView, LoginView, UpgradeStageView, PromocodeCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('upgrade-stage/', UpgradeStageView.as_view(), name='upgrade-stage'),
    path('create-promocode/', PromocodeCreateView.as_view(), name='create-promocode'),
]
