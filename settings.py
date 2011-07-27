class Settings:
    """
    This class contains every single thing that
    I'm not able to put in another class. For example,
    the command call options (quiet, test, delete..),
    the error messages, a list of extensions, and 
    stuff like that.
    """

    # Options
    quiet = False
    delete = False
    test = False

    # Extensions list
    exts = ['.mp3']

    # Error messages
    unknown_parameter = 'Unknown parameter! Try --help or -h to get some help'
    help_message = 'Music-paser, the tool that sort your musical library according to your tracks tags!\n\nusage: music-parser [arguments] [root folder ..]\narguments:\n-t   Print the changes in the console without applying them\n-q   Don\'t print the changes in the console while applying them\n-h   Display this help\n-d   Delete the files that aren\'t of a referenced musical extension'
    syntax_error = 'What did you try to do here?!'
    no_tag_error = 'It seems like your file is not tagged'

    def __init__(self, quiet=False, delete=False, test=True):
        self.quiet = quiet
        self.delete = delete
        self.test = test

