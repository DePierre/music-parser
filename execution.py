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
