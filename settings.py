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
    exts = ['.mp3', '.wav', '.wma', '.flac']

    # Error messages
    unknown_parameter = 'Unknown parameter! Try --help to get some help'
    help_message = 'This is the help message, supposed to help you!'
    syntax_error = 'What did you try to do here?!'
    no_tag_error = 'It seems like your file is not tagged'

    def __init__(self, quiet=False, delete=False, test=True):
        self.quiet = quiet
        self.delete = delete
        self.test = test

