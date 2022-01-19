import os


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        text = ''
        if os.path.isfile(self.file_path):
            with open(self.file_path) as f:
                text = f.read()
        return text
