import os, sys
from file_types import *
from settings import *

def execution(filebefore, fileafter):
    """
    We give to the execution function:
        - The old File_extension
        - The new File_extension (after parsing)
    And he makes magic come true with it
    """
    # 1st of all, we define the same tag for both
    filebefore.tag = fileafter.tag
    # 2ndly, we rename the file and move it
    if not Settings.quiet:
        print filebefore.path + filebefore.name + ' moved to ' + fileafter.path + fileafter.name
    os.renames(filebefore.path + filebefore.name, fileafter.path + fileafter.name)

def listfiles(path):
    """
    Return a list of files in the tree 
    at the 'path' location. Each object in the 
    list is composed of the name of the file + its path. 
    Return one list with musical files and another
    with every other files (images, mkv, nfo, nzb..)
    """
    # We create an initial musicfiles, non_musicfiles and directories list empty
    musicfiles = []
    non_musicfiles = []
    directories = []
    # We get a recursive list of all objects (folders, files...) contained
    # in the folder at the 'path' location
    wholelist = os.listdir(path)
    # Then, for each raw object:
    for it in wholelist:
        # If the raw object is a folder
        if os.path.isdir(path + '/' + it):
            # We call recursively the function on this folder
            musicfiles.extend(listfiles(path + '/' + it))
            directories.append(path + '/' + it)
        # Else if its already a files with an extension
        # present in the Settings.exts list of accepted extensions,
        elif os.path.splitext(path + '/' + it)[1] in Settings.exts:
            # We add it to the list with its path and name
            musicfiles.append(path + '/' + it)
        else:
            non_musicfiles.append(path + '/' + it)
    # Here you go, bitches, we return the music files, non_musicfiles
    # and every directory we found, for the empty ones to be deleted later on
    return [musicfiles, non_musicfiles, directories]

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
        if os.listdir(directory) == []:
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
