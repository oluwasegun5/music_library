from rest_framework.viewsets import ModelViewSet
from .models import Song,User
from .serializers import UserSerializers, SongSerializers
from  auths.serializers import UserCreateSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializers


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializers


