from os.path import isdir
from PyInquirer import prompt
from examples import custom_style_2
from counting.counter import WordCounter
from filesystem_dicts.file_dicts import *


class App(object):

    QUESTIONS = [

        {
            'type': 'input',
            'name': 'directory_choice',
            'message': 'Enter a directory.',
            'validate': lambda s: isdir(s) or 'Must enter a valid directory'
        }, 

        {
            'type': 'input',
            'name': 'words_choice',
            'message': 'Enter words to search'
        }

    ]

    def get_answers(self):
        self.answers = prompt(self.QUESTIONS, style=custom_style_2)
        self.chosen_dir = self.answers.get('directory_choice')
        self.chosen_words = self.answers.get('words_choice')

        return self.chosen_dir, self.chosen_words.split() # default is str, return list of words

    def get_dir_data(self, dir_: str) -> dict:
        self.dir_dict = DirDict(dir_)
        self.data = self.dir_dict.load_files()

        return self.data

    def count_words(self, words: list, data: dict) -> None:
        self.counter = WordCounter(words)
        self.counter.count(data)
        self.counter.print_top(10)

        return

    def run(self):
        print('welcome to the CLI word searcher!')
        self.chosen_dir, self.chosen_words = self.get_answers()
        
        self.data = self.get_dir_data(self.chosen_dir)
        self.count_words(self.chosen_words, self.data)

        return
