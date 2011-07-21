#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata
from file_types import *

def file_parser(file):
    """
    Global function to parse the new filename of the music file
    Use the properties of file_types to create:
        -the new name of the file
        -the new path of the file
    Return a file_types object which contains those datas
    """

    # Copy of the file instance to save it
    new_file = file
    # We find the right function depending on the extension of the file
    meta_func = find_meta_function(find_extension(file))
    return meta_func(new_file)
    
def find_extension(file):
    """
    Find the extension of the file.
    Return a string like 'mp3', 'wav', ...
    """

    index_ext = file.name.rfind('.')
    if index_ext != -1:
        return file.name[index_ext+1:]
    # else: we raise an exception because
    # we can't find any extension

def find_meta_function(ext):
    """
    Find the right set_meta_ext function if exist
    Return the name of the function as a string
    """

    func_name_key = 'set_meta_' + ext
    return globals()[func_name_key]
    # else: we raise an exception because
    # we don't know the format of the music file

def format_string(str):
    """
    Set special char 'éèêëàâäîï...' as 'eeeeaaaii...'
    and use str.title to format the string like a title.
    (i.e 'the wall' => 'The Wall')
    Return an ansi encoded string
    """

    return unicodedata.normalize('NFKD', unicode(str)).encode('ascii', 'ignore').title()


def build_path(elements):
    """
    Build the final path following this way:
        elements1 + '/' + elements2 + '/' + ...
    Return the fullpath as a string
    """

    fullpath = ''
    for elem in elements:
        fullpath += elem
        fullpath += '/'
    return fullpath[:-1]

def build_track_name(track, number = ''):
    """
    Build the track name with or without tracknumber.
    For instance :
        -track = 'Beat It'
        -number = '01'
        -trackname = '01 - Beat It'
    Return the trackname as a string
    """

    name = ''
    if number:
        name += number
        name += ' - '
    name += track
    return name

def set_meta_mp3(file):
    """
    Set new values of the file using tag id3
    This method uses different ones,
    to create the new values.
    Modifies the file with new values
    """

    file.tag["TITLE"] = format_string(file.tag["TITLE"])
    file.tag["ARTIST"] = format_string(file.tag["ARTIST"])
    file.tag["ALBUM"] = format_string(file.tag["ALBUM"])
    number = ''
    if "TRACKNUMBER" in vars(file.tag):
        number = file.tag["TRACKNUMBER"]
    else:
        pass
    file.name = build_track_name(file.tag["TITLE"], number) + '.mp3'
    file.path = build_path([file.tag["ARTIST"], file.tag["ALBUM"]])
    return file

