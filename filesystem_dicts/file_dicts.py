from collections.abc import MutableMapping
from parser.parser import Parser

class FileDict(MutableMapping):
    """A collection of contents corresponding to a specific file inside a directory."""
    def __init__(self, dir_name: str) -> None:
        """
        Initializes the class.
        Args:
            dir_name (str): directory name where the file is housed.
        """
        self.dir_name = dir_name
        self.data = {}
        self.parser = Parser(self.dir_name)
        
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


class DirDict(FileDict):

    def __init__(self, dir_name) -> None:
        super(DirDict, self).__init__(dir_name)


