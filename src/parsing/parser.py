import os
import re
import ntpath
import random # just to print samples of the set

class Parser(object):
    """Parses content of a file"""
    def __init__(self, full_path: str) -> None:
        """
        Initializes the class.
        Args:
            full_path (str): complete path to the file.
        """
        self.full_path = full_path
        self.dir_name, self.file_name = ntpath.split(self.full_path)

    def parse(self, file_: str=None) -> set:
        """
        Reads the file and saves the contents to a set.
        Args:
            file_ (str): another file name #gives possibility to parse another file from the same path
        Returns:
            set
        """
        if file_ is not None:
            self.file_name = file_
            self.full_path = os.path.join(self.dir_name, self.file_name)

        if not self._file_exists(self.full_path):
            raise FileNotFoundError('No such file or directory: {}'.format(self.full_path))

        with open(self.full_path) as f:
            # keeping only alphanumerical characters here
            # set since we only need one instance of each word (or number) to check if input is present
            self.data = {re.sub(r'[\W_]+', '', word.lower()) for line in f for word in line.split()}

        return self.data

    def write(self, output_path: str) -> None:
        """
        Writes the saved contents to another file. 
        Args:
            output_path (str): path to file where the contents will be saved.
        """
        output_dir = ntpath.split(output_path)[0]
        if not self._dir_exists(output_dir):
            print('Directory does not exist. Creating it...')
            os.makedirs(output_dir)

        set_as_str = ', '.join(self.data)

        with open(output_path, 'w') as f:
            f.write(set_as_str)

        return

    def _file_exists(self, file_: str) -> bool:
        """
        Checks if a file exists.
        Args:
            file_ (str): path and name to the file.
        Returns:
            bool.
        """
        return os.path.isfile(file_)

    def _dir_exists(self, dir_: str) -> bool:
        """
        Checks if a directory exists.
        Args:
            dir_ (str): directory name.
        Returns:
            bool.
        """
        return os.path.isdir(dir_)
