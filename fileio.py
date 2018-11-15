from pathlib import Path
import sys, os

sys.tracebacklimit = 0


class FileIO:
    def __init__(self, path):
        if isinstance(path, str):
            tmp_file = Path(path)
            if tmp_file.is_file():
                self.path = path
            else:
                raise IOError('File does not exist')
        else:
            raise ValueError('Incorrect TYPE, string is required')

    def write(self, data, type='w'):
        try:
            file = open(self.path, type)
            file.write(str(data))
        except IOError:
            raise IOError('Problem writing to file: ' + self.path)

    def read(self):
        try:
            file = open(self.path, 'r')
            return file.read()
        except IOError:
            raise IOError('Problem reading from file: ' + self.path)

    def return_list(self):
        try:
            src = open(self.path, 'r')
            return [line.rstrip() for line in src.readlines()]
        except IOError:
            raise IOError('Problem dealing with file: ' + self.path)

    def create(self, path):
        f = open(path, 'w+')
        f.close()

    def delete(self,path):
        os.remove(path)
