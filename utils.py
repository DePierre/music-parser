import os, sys
from file_types import *
from settings import *

def list_music_files(path):
    """
    Return a list of musical files in the tree 
    at the 'path' location. Each object in the 
    list is composed of the name of the file + its path. 
    """
    # We create an initial musicfiles empty
    music_files = []
    # We get a recursive list of all objects (folders, files...) contained
    # in the folder at the 'path' location
    wholelist = os.listdir(path)
    # Then, for each raw object:
    for it in wholelist:
        # If the raw object is a folder
        if os.path.isdir(path + '/' + it):
            # We call recursively the function on this folder
            music_files.extend(list_music_files(path + '/' + it))
        # Else if its already a files with an extension
        # present in the Settings.exts list of accepted extensions,
        elif os.path.splitext(path + '/' + it)[1] in Settings.exts:
            # We add it to the list with its path and name
            music_files.append(path + '/' + it)
    # Here you go, bitches, we return the music files
    return music_files

def list_not_music_files(path):
    """
    Return a list of non musical files in the tree 
    at the 'path' location. Each object in the 
    list is composed of the name of the file + its path. 
    For exemple: jpg, png, nfo, mkv, nzb...
    """
    # We create an initial not musical files empty
    not_music_files = []
    # We get a recursive list of all objects (folders, files...) contained
    # in the folder at the 'path' location
    wholelist = os.listdir(path)
    # Then, for each raw object:
    for it in wholelist:
        # If the raw object is a folder
        if os.path.isdir(path + '/' + it):
            # We call recursively the function on this folder
            not_music_files.extend(list_not_music_files(path + '/' + it))
        # Else if its already a files with an extension
        # present in the Settings.exts list of accepted extensions,
        elif os.path.splitext(path + '/' + it)[1] not in Settings.exts:
            # We add it to the list with its path and name
            not_music_files.append(path + '/' + it)
    # Here you go, bitches, we return the not_music_files
    return not_music_files

def list_directories(path):
    """
    Return a list of directories in the tree before modification 
    at the 'path' location. Each object in the 
    list is composed of the name of the file + its path. 
    Will help to delete empty directories at the end of the process
    """
    # We create an initial directories list empty
    directories = []
    # We get a recursive list of all objects (folders, files...) contained
    # in the folder at the 'path' location
    wholelist = os.listdir(path)
    # Then, for each raw object:
    for it in wholelist:
        # If the raw object is a folder
        if os.path.isdir(path + '/' + it):
            # We call recursively the function on this folder
            directories.extend(list_directories(path + '/' + it))
            directories.append(path + '/' + it)
    # Here you go, bitches, we return the directories list
    return directories

def delete_empty_directories(directories):
    """
    Will find every empty directories in the original
    tree of the directory we are working on and delete it.
    Only ancient directories can be empty, new ones
    have been created especially to put a file in it each single time
    """
    # First of all, we reverse the directories list
    # Because we need to first delete the high directories, which
    # were entered in the list after the low level directories
    # If you don't understand... go fuck yourself
    directories.reverse()
    # We create an initial empty list of empty directories (how ironic)
    empty_directories = []
    # And we test each one of the directories
    for directory in directories:
        # If the directory is empty
        if not os.listdir(directory):
            os.rmdir(directory)

def final_cleaning(non_musicfiles, directories):
    """
    Will clean the directory after having moved every
    files, including : deletion of non musical files if requested,
    plus deletion of empty directories in any case.
    """
    # If the user requested a deletion of all non musical files
    if Settings.delete:
        for it in non_musicfiles:
            os.remove(it)

    # We use the test function descibed above to look for empty directories
    # and delete them for us
    delete_empty_directories(directories)
