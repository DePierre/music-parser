from id3.ID3 import *

class File:
    """
    Abstract class.
    Represent the mother class of a music file, as follow:
        - mp3 (class : File_mp3)
        - wma (class : File_wma)
        - wav (class : File_wav)
        - flac (class : File_flac)
        - etc.
    Contains the name and path to a music file
    """
    name = ''
    path = ''
    def __init__(self, filenamewpath):
        # First of all, we split the file into a list of words
        # separated by a '/' character
        words = filenamewpath.rsplit('/')

        # Secondly, we take the last word of the list,
        # it's the name of the song. We delete it from the list
        self.name = words.pop()

        # Then we concatene each one of the words in the list,
        # those are the path folder names and put a '/' between them
        for word in words:
            self.path += word + '/'

class File_mp3(File):
    """
    Represent a MP3 file, inherit of the File class
    """
    def __init__(self, filenamewpath):
        File.__init__(self, filenamewpath)
        self.tag = ID3(self.path + self.name)
