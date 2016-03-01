class Song(object):
    """Simple class to store songs for the music player

    name: string name of a song
    age: string artist of a song
    """
    def __init__(self, name, artist, file_path):
        self.name = name
        self.artist = artist
        self.file_path = file_path
