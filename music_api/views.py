from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Song,User
from .serializers import UserSerializers, SongSerializers
from  auths.serializers import UserCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filter import SongFilter

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = SongFilter
    search_fields = ['title']



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializers

