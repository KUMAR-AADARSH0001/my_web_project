from django.urls import path
from hello import views
from hello.models import LogMessage

urlpatterns = [
    path("log/", views.homelistview),
]
