import ntpath
from os import listdir
from os.path import isfile, join, splitext
from collections.abc import MutableMapping
from parsing.parser import Parser

class FileDict(MutableMapping):
    """A collection of contents corresponding to a specific file."""
    def __init__(self, full_path: str) -> None:
        """
        Initializes the class.
        Args:
            dir_name (str): directory name where the file is housed.
        """
        self.full_path = full_path
        #self.dir_name, self.file_name = ntpath.split(self.full_path)
        self.data = {}
        self.parser = Parser(self.full_path)
        
    def __setitem__(self, key: str, value: str) -> None:
        """
        Sets a new key: value pair for a file. File will be parsed and the contents will be saved as value.
        Args:
            key (str): name to save the file content.
            value (str): file name.
        """
        self.data[key] = self.parser.parse(value)
        return

    def __getitem__(self, key: str) -> set:
        """
        Returns the file contents for a specific file.
        Args:
            key (str): name by which the content was saved.
        Returns:
            set.
        """
        return self.data[key]

    def __delitem__(self, key: str) -> None:
        """Removes a key: value pair."""
        del self.data[key]
        return

    def __len__(self) -> int:
        """Returns amount of files saved."""
        return len(self.data)

    def __iter__(self) -> iter:
        """Returns iterable of the object."""
        return iter(self.data)

    def __repr__(self) -> str:
        """Prints the object."""
        return f'FileDict{tuple(self.data.items())}'


class DirDict(object):
    """A collection of contents of each file for a specific directory"""

    def __init__(self, dir_name: str) -> None:
        self.dir_name = dir_name
        self.files = self.get_files_from_dir()
        self.file_dict = FileDict(self.dir_name)

    def get_files_from_dir(self) -> list:
        files = [f for f in listdir(self.dir_name) if isfile(join(self.dir_name, f))]
    
        return files

    def load_files(self) -> dict:
        for file in self.files:
            full_path = self.dir_name + file
            name, extension = splitext(file)
            self.file_dict[name] = full_path #parses full path and saves file content

        return self.file_dict.data
            
