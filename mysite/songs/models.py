from __future__ import unicode_literals

from django.db import models


class Song(models.Model):
    POP = 1
    ROCK = 2
    RAP = 3
    SONG_TYPES = (
        (POP, 'Pop'),
        (ROCK, 'Rock'),
        (RAP, 'Rap'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(blank=True, null=True)
    artist = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    length_secs = models.IntegerField(blank=True, null=True)
    song_type = models.PositiveSmallIntegerField(choices=SONG_TYPES, blank=True, null=True)
