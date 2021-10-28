from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from app_dir.main.api.views import UsersViewSet, BookmarksViewSet

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='users')
router.register('bookmarks', BookmarksViewSet, basename='bookmarks')

app_name = "api"

# import pprint
# pprint.pprint(router.get_urls())

urlpatterns = [
    path('', include(router.urls))
]