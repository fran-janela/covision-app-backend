from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from app_dir.main.api.views import BookmarksViewSet

router = routers.DefaultRouter()
router.register('bookmarks', BookmarksViewSet, basename='bookmarks')

app_name = "api"

# import pprint
# pprint.pprint(router.get_urls())

urlpatterns = [
    path('', include(router.urls))
]