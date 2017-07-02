from django import forms

from .models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'publication_date', 'artist', 'price', 'length_secs', 'song_type', )
