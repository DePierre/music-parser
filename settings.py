class Settings:
    quiet = False
    exts = ['.mp3', '.wav', '.wma', '.flac']
    delete = False

    def __init__(self, quiet, delete):
        self.quiet = quiet
        self.delete = delete
