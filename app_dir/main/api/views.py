from rest_framework.views import APIView
from rest_framework import viewsets, generics, filters
from ...core.loading import get_model
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from app_dir.main.api.serializers import BookmarksSerializer

class BookmarksViewSet(viewsets.ModelViewSet):
	TABLE = get_model('main', 'Bookmarks')
	queryset = TABLE.objects.all()
	serializer_class = BookmarksSerializer