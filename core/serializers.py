from rest_framework import serializers
from .models import HealthData

class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
        fields = ['heart_rate', 'o2_level']  # فقط این دو فیلد رو از JSON می‌گیریم، timestamp اتوماتیک اضافه می‌شه