from settings import *
import sys, os
from utils import list_music_files

def parse_command(argv):
    """
    Parse the command sent by the user.
    If an argument is not a parameter, then we add it to the
    list of paths. The function will return this list of paths
    and set the Settings class according to parameters set by user.
    """

    # We delete the first arg, which is the filename
    # <LOOOOOOOOOOOOOOOOOOL>
    argv.reverse()
    argv.pop()
    argv.reverse()
    # </LOOOOOOOOOOOOOOOOOOL>
    paths = []
    clean_paths = []
    for arg in argv:
        # If the argument is a directory
        if os.path.isdir(arg):
            # We add it to the paths list
            paths.append(arg)
        # If it looks like a parameter (with a - in front)
        elif arg[0] == '-':
            # We parse it to see the options and set them in Settings
            # If help is called by full word argument (--help),
            # We call if and cancel everything else
            if arg == '--help':
                # We print the help
                print Settings.help_message
                # And cancel everything else
                return []
            for param in arg:
                if param == 'q':
                    Settings.quiet = True
                elif param == 'd':
                    Settings.delete = True
                elif param == 't':
                    Settings.test = True
                # If help is called
                elif param == 'h':
                    # We print it
                    print Settings.help_message
                    # And cancel everything else
                    return []
                elif param == '-':
                    pass
                # If the option is not known, we print an error message
                else:
                    print Settings.unknown_parameter
        # If the argument is not a folder/parameter
        else: 
            # We print the error syntax message
            print Settings.syntax_error
            # And cancel everything else
            return []
    # The ending path '/' is not necessary. In a cleaning purpose we remove him,
    # that way, other functions can be based upon /path and not /path/ OR /path
    for path in paths:
        if path[-1] == '/':
            path = path[:-1]
        clean_paths.append(path)
    return clean_paths
