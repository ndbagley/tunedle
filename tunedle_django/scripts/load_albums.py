# Testing vscode git commit

from album_guesser.models import Album
import csv 

def run():
    with open('data/albums.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Album.objects.all().delete()

        for row in reader:
            print(row)

            album = Album(name=row[1], artist=row[2], image=row[3])
            album.save()