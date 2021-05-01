import os
import re
import ntpath
import random # just to print samples of the set

class Parser(object):

    def __init__(self, full_path: str) -> None:
        self.full_path = full_path
        self.dir_name, self.file_name = ntpath.split(self.full_path)

    def parse(self) -> set:
        if not self._file_exists(self.full_path):
            raise FileNotFoundError('No file named {} in {} directory'.format(self.file_name, self.dir_name))

        with open(self.full_path) as f:
            # keeping only alphanumerical characters here
            # set since we only need one instance of each word (or number) to check if input is present
            self.data = {re.sub(r'[\W_]+', '', word.lower()) for line in f for word in line.split()}

        return self.data

    def write(self, output_path: str) -> None:
        output_dir, output_file_name = ntpath.split(output_path)
        if not self._dir_exists(output_dir):
            print('Directory does not exist. Creating it...')
            os.mkdir(output_dir)

        with open(output_path, 'w') as f:
            f.write(self.data)

        return

    def _file_exists(self, file_name: str) -> bool:
        return os.path.isfile(file_name)

    def _dir_exists(self, dir_: str) -> bool:
        return os.path.isdir(dir_)

if __name__ == '__main__':
    #parser = Parser('../../inputs/doesntexist.txt')
    parser = Parser('../inputs/hamlet_TXT_FolgerShakespeare.txt')
    data = parser.parse()
    print(random.sample(data, 10))