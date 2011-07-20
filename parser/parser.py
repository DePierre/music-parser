#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Framework to parse music file's metadatas.

Expect a list of class File_extension, which contains path, filename and tag.
Return a dictionary like {'keys'='old filename': 'values'='new filename with fullpath', ...}"""

import os
import sys

class MusicFileParser(dict):
    "Dictionary like {'keys'='old filename': 'values'='new filename with fullpath', ...}"

    def __init__(self, listFile, rootPath='~/', ext='mp3'):
        self['ext'] = ext
        self['rpath'] = rootPath

    def __parse(self, listFile):
        for file in listFile:
            artist = file.artist.encode('ascii', 'replace')
            artist = artist.title()

            album = file.ablum.encode('ascii', 'replace')
            album = album.title()

            name = file.name.encore('ascii', 'replace')
            if name[:1].isdigit():
                tmp = name.partition(' ')
                if !tmp[0]:
                    numTrack = tmp[0]
                    numTrack += ' - '
                    name = numTrack + tmp[3]
            name = name.title()

            newFilename = self['rpath'] + '/' _
                          artist + '/' _
                          album + '/' _
                          name
            self[file.filename: newFilename]
    
