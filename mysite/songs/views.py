from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Song
from .forms import SongForm


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})


def save_song_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            songs = Song.objects.all()
            data['html_song_list'] = render_to_string('songs/includes/partial_song_list.html', {
                'songs': songs
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
    else:
        form = SongForm()
    return save_song_form(request, form, 'songs/includes/partial_song_create.html')


def song_update(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
    else:
        form = SongForm(instance=song)
    return save_song_form(request, form, 'songs/includes/partial_song_update.html')


def song_delete(request, pk):
    song = get_object_or_404(Song, pk=pk)
    data = dict()
    if request.method == 'POST':
        song.delete()
        data['form_is_valid'] = True
        songs = Song.objects.all()
        data['html_song_list'] = render_to_string('songs/includes/partial_song_list.html', {
            'songs': songs
        })
    else:
        context = {'song': song}
        data['html_form'] = render_to_string('songs/includes/partial_song_delete.html', context, request=request)
    return JsonResponse(data)
