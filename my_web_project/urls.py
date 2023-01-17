from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("hello.urls")),
]
urlpatterns += staticfiles_urlpatterns()
