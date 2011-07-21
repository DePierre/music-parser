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
    Return a dict which contains those datas
    """

    # Copy of the file instance to save it
    new_file = file
    # We find the right function depending on the extension of the file
    meta_func = find_meta_function(find_extension(file))
    dict_file = meta_func(new_file)
    return dict_file
    
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
    This functions uses different ones,
    to create the new values.
    Return a dict with new values
    """

    dict_file = {}
    if file.tag.d.has_key("TITLE"):
        dict_file['title'] = format_string(file.tag["TITLE"])
    else:
        dict_file['title'] = 'Unknow'
    if file.tag.d.has_key("ARTIST"):
        dict_file['artist'] = format_string(file.tag["ARTIST"])
    else:
        dict_file['artist'] = 'Unknow'
    if file.tag.d.has_key("ALBUM"): 
        dict_file['album'] = format_string(file.tag["ALBUM"])
    else:
        dict_file['artist'] = 'Unknow'
    number = ''
    if file.tag.has_key("TRACKNUMBER"):
        number = file.tag["TRACKNUMBER"]
    dict_file['tracknumber'] = number
    dict_file['name'] = build_track_name(dict_file['album'], number) + '.mp3'
    dict_file['path'] = build_path([dict_file['artist'], file.tag["ALBUM"]])
    if file.tag.d.has_key("YEAR"):
        dict_file['year'] = file.tag["YEAR"]
    if file.tag.d.has_key("COMMENT"):
        dict_file['comment'] = file.tag["COMMENT"]
    if file.tag.d.has_key("GENRE"):
        dict_file['genre'] = file.tag["GENRE"]
    return dict_file

