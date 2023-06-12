from django.shortcuts import render, redirect
from .models import Album, Guess
from .forms import MakeGuess
from django.contrib import messages
import datetime

start = datetime.date(2023, 6, 8)
delta = datetime.date.today() - start 

def home(request):
    album_obj = Album.objects.all()[delta.days % len(Album.objects.all())]
    artists = Album.objects.values_list('artist', flat=True).distinct()
    albums = Album.objects.values_list('name', flat=True).distinct()
    if request.method == 'POST':
        form = MakeGuess(request.POST)
        artist = form['artist'].value()
        album = form['album'].value()
        if artist == album_obj.artist and album == album_obj.name:
            messages.success(request, 'Yay baby good job!')
        else:
            messages.error(request, 'Damn Serena are you retarded?!')
        return redirect('tunedle-home')
    else:
        form = MakeGuess()

    context = {
        'album': album_obj,
        'form': form,
        'artists': artists,
        'albums': albums,
        'title': 'Daily',
    }
    return render(request, 'album_guesser/home.html', context)

def about(request):
    return render(request, 'album_guesser/about.html')


