from django.urls import path
from django.http import JsonResponse
def home(request): return JsonResponse({'status':'ok'})
urlpatterns = [path('', home)]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
]
