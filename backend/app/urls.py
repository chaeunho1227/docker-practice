from django.urls import path, include
from .views import html

app_name = "app"

urlpatterns = [
    path('', html, name="html"),
]