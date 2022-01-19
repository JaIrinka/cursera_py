import os.path
import tempfile


class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        if not os.path.exists(path_to_file):
            self.write()
        self.current = 0

    def write(self, new_str=''):
        f = open(self.path_to_file, 'w')
        f.write(new_str)
        f.close()

    def read(self):
        f = open(self.path_to_file, 'r')
        content = f.read()
        f.close()
        return content

    def __str__(self):
        return self.path_to_file

    def __add__(self, other):
        new_file = tempfile.NamedTemporaryFile(delete=False)
        new_file_obj = File(new_file.name)
        f1_content = self.read()
        f2_content = other.read()
        new_file_obj.write(f1_content + f2_content)
        return new_file_obj

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path_to_file, 'r') as file:
            self.lines = file.readlines()

        if self.current >= len(self.lines):
            self.current = 0
            raise StopIteration

        result = self.lines[self.current]
        self.current += 1
        return result
