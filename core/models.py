from django.db import models

class HealthData(models.Model):
    heart_rate = models.IntegerField()  # ضربان قلب
    o2_level = models.IntegerField()    # میزان اکسیژن
    timestamp = models.DateTimeField(auto_now_add=True)  # زمان اتوماتیک

    def __str__(self):
        return f"HR: {self.heart_rate}, O2: {self.o2_level} at {self.timestamp}"