from rest_framework import serializers
from .models import HealthData

class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
        fields = [
            'device_id',
            'finger_detected',
            'heart_rate',
            'o2_level',  # فیلد جدید
            'ir_value',
            'signal_quality',
            'test_counter',
            'test_mode',
            'timestamp'
        ]
        extra_kwargs = {
            'device_id': {'required': False, 'allow_null': True},
            'finger_detected': {'required': False, 'allow_null': True},
            'heart_rate': {'required': True},
            'o2_level': {'required': False, 'allow_null': True},  # موقتاً اختیاری
            'ir_value': {'required': False, 'allow_null': True},
            'signal_quality': {'required': False, 'allow_null': True},
            'test_counter': {'required': False, 'allow_null': True},
            'test_mode': {'required': False, 'allow_null': True},
            'timestamp': {'required': False, 'allow_null': True},
        }