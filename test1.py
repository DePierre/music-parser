from id3.ID3 import *
from file_types import File_mp3
import sys

for arg in sys.argv:
    if not arg == 'test1.py':
        file1 = File_mp3(arg)
        print file1.tag['ARTIST']
