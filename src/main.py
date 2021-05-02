from parsing.parser import Parser
from counting.counter import WordCounter
from filesystem_dicts.file_dicts import *


def main() -> None:
    dir_dict = DirDict('../inputs/')
    #print(dir_dict.files)
    data = dir_dict.load_files()
    #print(data.keys())
    #print(data.values())
    
    counter = WordCounter(['shadows', 'offended', 'mended', 'command'])
    counter.count(data)
    counter.print_top(10)


    return

if __name__ == '__main__':
    main()
