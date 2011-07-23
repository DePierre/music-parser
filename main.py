#! /usr/bin/env python

"""
Main function, will use every
modules and functiosn created
Take the command arguments and manage them
"""

import os, sys
from command import parse_command
from settings import Settings
from parser import *
from file_types import *
from utils import *
from execution import *

# First step : We parse and set the command sent by the user
# We will store the settings in the Settings class (settings.py)
# For exemple : quiet or not (-q arg), delete the non music track files or not (-d)
# Also, an argument -t which allow to just print the incoming changes, not
# apply them
# We get arguments from user
list_root_path = parse_command(sys.argv)
# Second step : We use listfiles to recursively get all the files
# present in the tree with the specified folder as root
# Last arg have to be the root path.
# As you know, options start with '-',
# but the root path doesn't
# We get lists of all what we'll need into each root_path given by the user
for root_path in list_root_path:
    l_music_files = list_music_files(root_path)
    l_not_music_files = list_not_music_files(root_path)
    l_directories = list_directories(root_path)
# Third step : We create a loop which will, for each file:
#   - Parse it with the Parser (parser.py)
#   - Take the File_ext given by the parser and execute the execution function
    for music_file in l_music_files:
        # We get a dictionnary of all new value properties of the current file
        instant_file = File_mp3(music_file)
        dict_new_prop = file_parser(instant_file)
        execution(instant_file, dict_new_prop)
# Fourth step : We delete (if indicated in the settings file) all non musical files,
# files which in case did not move. Plus, we need to delete every empty folder in the 
# tree. For that, we use final_cleaning from utils.py
    if Settings.delete:
        final_cleaning(l_not_music_files, l_directories)

