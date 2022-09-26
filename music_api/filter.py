from music_api.models import Song
from django_filters import FilterSet

class SongFilter(FilterSet):
    class Meta:
        model = Song
        fields = {
            'name':['exact']
        }
