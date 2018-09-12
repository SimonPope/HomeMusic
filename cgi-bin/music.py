from threading import Thread
import subprocess
import os
import cgi
import cgitb
cgitb.enable()

foobar = r'C:\Program Files (x86)\foobar2000\foobar2000.exe'
musicFolder = r'F:\Music'
silence = 'assets/silence.mp3'
arguments = cgi.FieldStorage()

def display():
    print('Content-type: text/html\n')
    print('<script src="../scripts/navigation.js"></script>')
    print("<html>")
    print('<title>Music</title>')
    print("""<link type="text/css" rel="stylesheet" href="../css/stylesheet.css"/>""")
    print('<body>')

    if 'song' in arguments:
        play(arguments["artist"].value, arguments["album"].value, arguments["song"].value)
    elif 'album' in arguments:
        songs(arguments["artist"].value, arguments["album"].value)
    elif 'artist' in arguments:
        albums(arguments["artist"].value)
    else:
        artists()

    print('</body>')
    print("</html>")

def artists():
    for artist in os.listdir(musicFolder):
        if (os.path.isdir(os.path.join(musicFolder, artist))):
            print('<button onClick="goToArtist(this.innerHTML)">')
            print(artist)
            print('</button>')

def albums(artist):
    artistFolder = os.path.join(musicFolder, artist)
    for album in os.listdir(artistFolder):
        if (os.path.isdir(os.path.join(artistFolder, album))):
            print('<button id="' + artist + '" onClick="goToAlbum(this.id, this.innerHTML)">')
            print(album)
            print('</button>')

def songs(artist, album):
    for song in os.listdir(os.path.join(musicFolder, artist, album)):
        filetype = song[(song.rfind('.') + 1):]
        if filetype == 'mp3' or filetype == 'm4a' or filetype == 'wma' or filetype == 'flac':
            split = song.split('.')
            print('<button id="artist=' + artist + '&album=' + album + '&song=' + song + '" onClick="goToSong(this.id)">')
            print(split[0])
            print('</button>')

def play(artist, album, firstSong):
    albumFolder = os.path.join(musicFolder, artist, album)
    playArgs = [foobar, silence]
    found = False
    for song in os.listdir(albumFolder):
        if found:
            filetype = song[(song.rfind('.') + 1):]
            if filetype == 'mp3' or filetype == 'm4a' or filetype == 'wma' or filetype == 'flac':
                playArgs.append(os.path.join(albumFolder, song))
        elif song == firstSong:
            found = True
            playArgs.append(os.path.join(albumFolder, song))
    Thread(target=subprocess.Popen, args=[playArgs]).start()
    print('<div class="playing">')
    print('<h1 class="playing">Now playing:<br>' + artist + '<br>' + album + '<br>' + firstSong.split('.')[0] + '</h1>')
    print('</div>')

display()