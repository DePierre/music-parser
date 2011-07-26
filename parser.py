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
    dict_file = {}
    # We find the right function depending on the extension of the file
    meta_func = find_meta_function(find_extension(file))
    if callable(meta_func):
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

def delete_spe_char_and_format(str):
    """
    Set special char 'éèêëàâäîï...' as 'eeeeaaaii...',
    all char "'-_/..." are replaced by ' '
    and use str.title to format the string like a title.
    (i.e 'the wall' => 'The Wall')
    Return an ansi encoded string
    """

    # new_str = unicodedata.normalize('NFKD', unicode(str)).encode('ascii', 'ignore').title()
    new_str = str.title()
    for i in range(len(new_str)):
        # If it's not a alphanumeric char
        # it's probably a char like "'-_/..."
        if not new_str[i].isalnum():
            new_str.replace(new_str[i], ' ', 1)
    return new_str

def strip_not_alnum_char(str):
    """
    Delete from the begin all not alnum char
    Return the final string
    """

    i = 0
    # While we don't find a character or a digit,
    # that means it's a special char (logical!)
    if str:
        while not str[i].isalnum() and i < len(str) - 1:
            i += 1
        if i != len(str) - 2:
            str = str[i:]
    return str

def delete_duplicate(str, list_dup):
    """
    Delete duplicate string from str with list_dup.
    For instance, 'title' could be like :
    'Deep Purple - Smoke On The Water'
    So this function will remove 'Deep Purple' from 'title'
    because list_dup contains 'Deep Purple'.
    Return the new 'title'
    """

    for dup in list_dup:
        str = str.lstrip(dup)
        if not str:
            str = dup
        str = strip_not_alnum_char(str)
    return str

def find_tracknumber(title):
    """
    Try to find the track_number of the music file.
    Even if ID3 didn't find it,
    maybe this function can.
    Return the tracknumber as a string
    """

    tracknumber = ''
    # If we found a digit, it's probably the tracknumber
    j = 0
    # So we save it into tracknumber
    while title[j].isdigit() and j < len(title):
        tracknumber += title[j]
        j += 1
    return tracknumber

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

    list_str_prop_mp3 = ['album', 'artist', 'title']
    list_other_prop_mp3 = ['comment', 'genre', 'year']
    dict_file_mp3 = {}
    # For each string properties into the tag
    for prop in list_str_prop_mp3:
        # If the tag exist (i.e it's not empty for the music file)
        if file.tag.d.has_key(prop.upper()):
            # We delete spe char and we format it
            dict_file_mp3[prop] = delete_spe_char_and_format(file.tag[prop.upper()])
        else:
            # Or we define it's value as 'Unknow ' + prop
            # For instance 'Unknow Artist'
            dict_file_mp3[prop] = 'Unknow ' + prop.capitalize()
    # For each other properties
    for prop in list_other_prop_mp3:
        if file.tag.d.has_key(prop.upper()):
            # We just copy them
            dict_file_mp3[prop] = file.tag[prop.upper()]
        else:
            dict_file_mp3[prop] = ''
    # To try to find the tracknumber, we need 'title'
    if dict_file_mp3.has_key('title'): 
        # But before, we delete the duplicate
        list_duplicate = [dict_file_mp3['artist'], dict_file_mp3['album']]
        # Now we delete the duplicates
        dict_file_mp3['title'] = delete_duplicate(dict_file_mp3['title'], list_duplicate)
        # So we are able to find the tracknumber
        number = ''
        # If ID3 already find it
        if file.tag.d.has_key("TRACKNUMBER"):
            number = file.tag["TRACKNUMBER"]
        # Else we try to find by ourself
        else:
            number = find_tracknumber(dict_file_mp3['title'])
            # If we found a tracknumber, we delete it from 'title'
            if number:
                dict_file_mp3['title'] = delete_duplicate(dict_file_mp3['title'], [number])
        dict_file_mp3['tracknumber'] = number
        # And we format the new title
        dict_file_mp3['title'] = build_track_name(dict_file_mp3['title'], number)
    dict_file_mp3['name'] = dict_file_mp3['title'] + '.mp3'
    dict_file_mp3['path'] = build_path([dict_file_mp3['artist'], dict_file_mp3['album']])
    return dict_file_mp3

