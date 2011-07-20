#! /usr/bin/env python

def getProperString(oldString):
    properString = oldString.encode('ascii', 'replace')
    properString = properString.title()
                    
    return properString
                    
def getTrackName(track, number = ''):
    name = ''
    if number:
        name += number
        name += ' - '
    name += track
                     
    return name
                                
def getPath(elements):
    fullpath = ''
    for elem in elements:
        fullpath += elem
        fullpath += '/'
    fullpath = fullpath.rstrip('/')
    
    return fullpath
                      
from id3.ID3 import *
from file_types import *

class MusicFileParser(list):
    """
    blabla
    """
                                                        
    def __init__(self, file):
        self.filename = getProperString(file.name)
        self.path = file.path.encode('ascii', 'replace')
        self.path = self.path.rstrip('/')
                                                                        
class MusicFileParser_mp3(MusicFileParser):
    """
    blabla
    """
                                                                                        
    def __init__(self, file):
        MusicFileParser.__init__(self, file)
        self.artist = getProperString(file.tag["ARTIST"])
        self.album = getProperString(file.tag["ALBUM"])
        #try:
        #self.name = getTrackName(file.tag["TITLE"], file.tag["TRACKNUMBER"])
        #finally:
        #self.name = getTrackName(file.tag["TITLE"])
        self.name = getTrackName(file.tag["TITLE"])     
        self.fullpath = getPath((self.path, self.artist, self.album, self.name))
