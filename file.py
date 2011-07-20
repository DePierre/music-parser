from id3.ID3 import *

class File:
    """
    Abstract class.
    Represent the base of specific music files like:
        - flac (class name : File_flac)
        - mp3 (class name : File_mp3)
        - wav (class name : File_wav)
        - wma
        - etc.
    """
    def __init__(self, filenamewpath)
        # We split the whole filename and its path 
        words = arg.rsplit('/')

        # We set the name of the filename by using
        # the 'word' after the last / (which is the separator)
        self.name = words.pop()

        # We set the path of the filename by concatening every
        # word of the words list and we put the '/' back in it
        self.path = ''
        for word in words:
            path += word + '/'
