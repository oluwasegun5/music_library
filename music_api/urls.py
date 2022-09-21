from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

app_name = "music"

router = SimpleRouter()
router.register('songs',views.SongViewSet)
router.register('users',views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]


