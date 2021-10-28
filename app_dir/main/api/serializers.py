from rest_framework import serializers
from django.db.models import fields
from ...core.loading import get_model
from app_dir.main.models import Bookmark, User

APP = 'main_api'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookmarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'