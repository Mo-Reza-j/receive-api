from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import HealthData
from .serializers import HealthDataSerializer
import logging

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')  # غیرفعال کردن CSRF
class HealthDataCreateView(generics.CreateAPIView):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            logger.info(f"Received data: {request.data}")
            return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)
        logger.error(f"Invalid data: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HealthDataListView(generics.ListAPIView):
    queryset = HealthData.objects.all().order_by('-timestamp')
    serializer_class = HealthDataSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()[:10]
        serializer = self.get_serializer(queryset, many=True)
        logger.info("Fetched health data list")
        return Response(serializer.data)