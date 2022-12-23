from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# Create your views here.

my_playlists=[
    {"id":1,"name":"Car Playlist","numberOfSongs":4},
    {"id":2,"name":"Coding Playlist","numberOfSongs":2}
]

def home(request):
    return render(request, 'zing_it/home.html',{"my_playlists":my_playlists})
my_songs = [
            {"id": 1, "Track": "thank u, next", "Artist": "Ariana Grande", "Album": "thank u, next", "Length": "3:27","playlist_id": 1},
            {"id": 2, "Track": "One Kiss, next", "Artist": "Dua Lipa, Calvin Harris", "Album": "One Kiss", "Length": "3:34","playlist_id": 1},
            {"id": 3, "Track": "Better Now", "Artist": "Post Malone", "Album": "beerbongs & bentleys", "Length": "3:51","playlist_id": 1},
            {"id": 4, "Track": "The Middle", "Artist": "Grey,Marren Morris, ZEDD", "Album": "The Middle", "Length": "3:04","playlist_id": 1},
            {"id": 5, "Track": "Love Lies", "Artist": "Normani, Khalid", "Album": "Love Lies", "Length": "3:21","playlist_id": 2},
            {"id": 6, "Track": "Rise", "Artist": "Jack & Jack, Jonas Blue", "Album": "Blue", "Length": "3:14","playlist_id": 2},
    ]

def playlist(request, id):
    songs=[]
    playlist_name=''
    for playlist in my_playlists:
        if(id == playlist['id']):
            playlist_name = playlist['name']
    
    if len(playlist_name) == 0:
        raise Http404("No such a playlist exist")
    
    for song in my_songs:
        if(id == song['playlist_id']):
            songs.append(song)
    
    return render(request, 'zing_it/songs.html', {"songs":songs,"playlist_name":playlist_name})
