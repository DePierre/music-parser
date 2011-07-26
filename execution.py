import os, sys
import copy
from file_types import *
from settings import *

def execution(filebefore, dict_file_after):
    """
    We give to the execution function:
        - The old File_extension
        - The new File_extension's dict (after parsing)
    And he makes magic come true with it
    """
    # 1st of all, we define the same tag for both
    # We delete properties which aren't in the ID3's tag
    dict_tag = dict_file_after.copy()
    del dict_tag['name']
    del dict_tag['path']
    # We define the new tag
    for key in dict_tag:
        filebefore.tag[key] = dict_tag[key]
    # 2ndly, we rename the file and move it
    if not Settings.quiet:
        print filebefore.path + '/' + filebefore.name + ' moved to ' + dict_file_after['path'] + '/' + dict_file_after['name']
    if not Settings.test:
    os.renames(filebefore.path + '/' + filebefore.name, dict_file_after['path'] + '/' + dict_file_after['name'])
