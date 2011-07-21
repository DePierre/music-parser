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
    """
    # We create an initial files list empty
    files = []
    # We get a recursive list of all objects (folders, files...) contained
    # in the folder at the 'path' location
    wholelist = os.listdir(path)
    # Then, for each raw object:
    for it in wholelist:
        # If the raw object is a folder
        if os.path.isdir(path + '/' + it):
            # We call recursively the function on this folder
            files.extend(listfiles(path + '/' + it))
        # Else if its already a files with an extension
        # present in the Settings.exts list of accepted extensions,
        elif os.path.splitext(path + '/' + it)[1] in Settings.exts:
            # We add it to the list with its path and name
            files.append(path + '/' + it)
    # Here you go, bitches!
    return files
