
from django.urls import include, path
from django.contrib import admin
from django.http import JsonResponse


def index(request):
    return JsonResponse({'msg': 'Sample Web project'})


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path("", include("hello.urls")),
]
