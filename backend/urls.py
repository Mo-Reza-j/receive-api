from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Health Monitor API. Use /api/health-data/ for POST requests.")

urlpatterns = [
    path('', home, name='home'),  # مسیر ریشه
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]