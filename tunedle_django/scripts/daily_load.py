from album_guesser.models import Album
import csv
from datetime import datetime

def run():

    al_inuse = Album.objects.all().filter(cur_album=True)
    al_inuse(already_used=True, cur_album=False)
    new_album = Album.objects.all().filter(already_used=False).first()
    new_album(cur_album=True)
    al_inuse.save()
    new_album.save()
