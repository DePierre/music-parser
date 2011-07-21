from id3.ID3 import *
import os

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
    def __init__(self, filenamewpath):
        self.name = os.path.basename(filenamewpath)
        self.path = os.path.dirname(filenamewpath)

class File_mp3(File):
    """
    Represent a MP3 file, inherit of the File class
    """
    def __init__(self, filenamewpath):
        File.__init__(self, filenamewpath)
        self.tag = ID3(self.path + '/' +  self.name)
