from django.shortcuts import render, redirect
from .models import Album, Guess
from .forms import MakeGuess
from django.contrib import messages


def home(request):
    album_obj = Album.objects.all().filter(date_used=None).first()
    if request.method == 'POST':
        form = MakeGuess(request.POST)
        guess = form['guess'].value()
        if guess == album_obj.name:
            messages.success(request, 'You got it!')

        else:
            messages.error(request, 'Wrong!')
        return redirect('tunedle-home')
    else:
        form = MakeGuess()

    context = {
        'album': album_obj,
        'form': form,
        'title': 'Daily'
    }
    return render(request, 'album_guesser/home.html', context)

def about(request):
    return render(request, 'album_guesser/about.html')

