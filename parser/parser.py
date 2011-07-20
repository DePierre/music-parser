#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Framework to parse music file's metadatas.

Expect a list of class File_extension, which contains path, filename and tag.
Return a dictionary like {'keys'='old filename': 'values'='new filename with fullpath', ...}"""

class MusicFileParser(dict):
    "Dictionary like {'keys'='old filename': 'values'='new filename with fullpath', ...}"

    def __parse(self, listFile, rootPath='~/'):
        for file in listFile:
            #Delete specials characters like 'éèàïîäâ...'
            artist = file.artist.encode('ascii', 'replace')
            #Firt letter of all words are uppercased
            artist = artist.title()

            album = file.ablum.encode('ascii', 'replace')
            album = album.title()

            name = file.name.encore('ascii', 'replace')
            #If the begin of the word is a digit (number of the tracklist)
            if name[:1].isdigit():
                tmp = name.partition(' ')
                #And if we can get this digit
                if not tmp[1]:
                    numTrack = tmp[0]
                    numTrack += ' - '
                    name = numTrack + tmp[3]
            name = name.title()

            newFilename = rootPath + '/' _
                          artist + '/' _
                          album + '/' _
                          name
            self[file.filename: newFilename]
    
