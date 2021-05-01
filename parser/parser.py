import os
import re
import ntpath
import random # just to print samples of the set

class Parser(object):

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.dir_name, self.file_name = ntpath.split(file_path)

    
    def parse(self) -> list:
        if not self._file_exists(self.file_path):
            raise FileNotFoundError('No file named {} in directory {}'.format(self.file_name, self.dir_name))

        with open(self.file_path) as f:
            # keeping only alphanumerical characters here
            # set since we only need one instance of each word (or number) to check if input is present
            self.data = {re.sub(r'[\W_]+', '', word.lower()) for line in f for word in line.split()}

        return self.data

    def write(self, output_path: str) -> None:
        output_dir, output_file_name = ntpath.split(output_path)
        if not self._dir_exists(output_dir):
            raise FileNotFoundError('Directory {} does not exist'.format(output_dir))

        with open(output_path, 'w') as f:
            f.write(self.data)

        return

    def _file_exists(self, file_name: str) -> bool:
        return os.path.isfile(file_name)

    def _dir_exists(self, dir_: str) -> bool:
        return os.path.isdir(dir_)

if __name__ == '__main__':
    #parser = Parser('../inputs/hamlet_TXT_FolgerShakespeare.txt')
    parser = Parser('wrong_input.txt')
    data = parser.parse()
    print(random.sample(data, 10))
