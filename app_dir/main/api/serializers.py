from rest_framework import serializers
from django.db.models import fields
from ...core.loading import get_model
from app_dir.main.models import Bookmarks

APP = 'main_api'

class BookmarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = '__all__'