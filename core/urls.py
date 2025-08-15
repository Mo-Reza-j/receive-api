from django.urls import path
from .views import HealthDataCreateView

urlpatterns = [
    path('health-data/', HealthDataCreateView.as_view(), name='health-data-create'),
]