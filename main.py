"""
Main function, will use every
modules and functiosn created
Take the command arguments and manage them
"""

import os, sys

# First step : We parse and set the command sent by the user
# We will store the settings in the Settings class (settings.py)
# For exemple : quiet or not (-q arg), delete the non music track files or not (-d)
# Also, an argument -t which allow to just print the incoming changes, not
# apply them

# Second step : We use listfiles to recursively get all the files
# present in the tree with the specified folder as root

# Third step : We create a loop which will, for each file:
#   - Parse it with the Parser (parser.py)
#   - Take the File_ext given by the parser and execute the execution function

# Fourth step : We delete (if indicated in the settings file) all non musical files,
# files which in case did not move. Plus, we need to delete every empty folder in the 
# tree. For that, we use final_cleaning from utils.py
