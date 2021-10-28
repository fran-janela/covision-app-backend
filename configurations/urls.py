from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include(('app_dir.main.api.urls', 'main_api'), namespace='main_api')),
]

