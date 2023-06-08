# Testing vscode git commit

from album_guesser.models import Album
import csv

def run():
    with open('data/albums3.csv') as file:
        reader = csv.reader(file)
        next(reader)


        """ 
        Do we want to delete all the objects? 
        Probaby want to just add them and then filter out repeat albums
        """
        #Album.objects.all().delete()

        for row in reader:
            print(row)

            album = Album(name=row[1], artist=row[2], image=row[3])
            album.save()

    for album in Album.objects.values_list('name', flat=True).distinct():
        Album.objects.filter(pk__in=Album.objects.filter(name=album).values_list('id', flat=True)[1:]).delete()
 
