from pathlib import Path
import sys, os

sys.tracebacklimit = 0


class FileIO:
    file = None
    path = None


    def set_path(self,path):
        if isinstance(path, str):
            if self.directory_exists(path):
                self.path = path
            else:
                raise IOError('Directory does not exist')
        else:
            raise ValueError('Incorrect TYPE, string is required')

    def set_file(self,file):
        if isinstance(file, str):
            if self.directory_exists(file):
                self.file = file
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

    def read_list(self):
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

    def directory_exists(self, path):
        return os.path.isdir(path)

    def directory_is_set(self):
        return self.path != None

    def file_exists(self, file):
        return os.path.exists(file)

    def file_is_set(self):
        return self.file != None

    def get_path(self):
        if self.directory_is_set():
            return self.path
        raise Exception('Directory has not been set.')

    def get_file(self):
        if self.file_is_set():
            return self.file
        raise Exception('File name has not been set.')

