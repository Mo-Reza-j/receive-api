from django.db import models

class HealthData(models.Model):
    device_id = models.CharField(max_length=50, blank=True, null=True)
    finger_detected = models.BooleanField(default=False)
    heart_rate = models.IntegerField()
    o2_level = models.IntegerField(blank=True, null=True)  # فیلد جدید
    ir_value = models.IntegerField(blank=True, null=True)
    signal_quality = models.CharField(max_length=20, blank=True, null=True)
    test_counter = models.IntegerField(blank=True, null=True)
    test_mode = models.BooleanField(default=False)
    timestamp = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Device {self.device_id}: HR={self.heart_rate}, O2={self.o2_level}, IR={self.ir_value} at {self.created_at}"