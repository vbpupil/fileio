import os


class FileIO:
    def __init__(self, path):
        if isinstance(path, str):
            self.path = path
        else:
            raise ValueError('Incorrect TYPE, expecting str')

    def write(self, data, type='w'):
        try:
            file = open(self.path, type)
            file.write(str(data))
        except IOError:
            raise IOError('Problem dealing with file: ' + self.path)

    def read(self):
        try:
            file = open(self.path, 'r')
            return file.read()
        except IOError:
            raise IOError('Problem dealing with file: ' + self.path)

    def return_list(self):
        try:
            src = open(self.path, 'r')
            return [line.rstrip() for line in src.readlines()]
        except IOError:
            raise IOError('Problem dealing with file: ' + self.path)
