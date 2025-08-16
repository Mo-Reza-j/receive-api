from django.contrib import admin
from .models import HealthData

@admin.register(HealthData)
class HealthDataAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'heart_rate', 'o2_level', 'ir_value', 'signal_quality', 'timestamp', 'created_at')
    list_filter = ('device_id', 'test_mode', 'created_at')
    search_fields = ('device_id', 'signal_quality')