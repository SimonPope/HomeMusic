function goToArtist(artist) {
    window.location.href = 'music.py?artist=' + artist;
}

function goToAlbum(artist, album) {
    window.location.href = 'music.py?artist=' + artist + '&album=' + album;
}

function goToSong(args) {
    window.location.href = 'music.py?' + args;
}