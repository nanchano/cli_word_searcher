from os.path import isdir
from PyInquirer import prompt
from examples import custom_style_2
from counting.counter import WordCounter
from filesystem_dicts.file_dicts import *
from prompt_toolkit.validation import Validator, ValidationError

class App(object):
    """CLI Application."""
    START_QUESTION = [
        {
            'type': 'list',
            'name': 'start_options',
            'message': 'Select an option.',
            'choices': ['Search', 'Help', 'Exit'],
        }
    ]

    QUESTIONS = [
        {
            'type': 'input',
            'name': 'directory_choice',
            'message': 'Enter a directory.',
            'validate': lambda s: isdir(s) or 'Directory does not exist. Must enter a valid directory'
        }, 
        {
            'type': 'input',
            'name': 'words_choice',
            'message': 'Enter words to search.'
        }

    ]

    def _print_help(self):
        """Prints help message."""
        msg = '''A CLI tool that searches words inside the files on a given directory and ranks them based on their presence ratio, returning a list of the top 10 files that contain the most words.'''
        print(msg)

        return

    def _eval_start_options(self):
        """Evauates starting options based on user input."""
        ans = prompt(self.START_QUESTION, style=custom_style_2).get('start_options')

        if ans == 'Exit':
            exit()
        elif ans == 'Help':
            self._print_help()
        else:
            return


    def get_answers(self):
        """Get answers based on user responses to the prompts."""
        self.answers = prompt(self.QUESTIONS, style=custom_style_2)

        self.chosen_dir = self.answers.get('directory_choice')
        self.chosen_words = self.answers.get('words_choice')

        return self.chosen_dir, self.chosen_words.split() # default is str, return list of words

    def get_dir_data(self, dir_: str) -> dict:
        """Gets each file data on the directory
        Args:
            dir_ (str): directory to search on.
        Returns:
            dict
        """
        self.dir_dict = DirDict(dir_)
        self.data = self.dir_dict.load_files()

        return self.data

    def count_words(self, words: list, data: dict) -> None:
        """
        Count each word on each file.
        Args:
            words (list): elements to search.
            data (dict): data to search on.
        """
        self.counter = WordCounter(words)
        self.counter.count(data)
        self.counter.print_top(10)

        return

    def run(self):
        """Runs the app."""
        print('welcome to the CLI word searcher!')

        self._eval_start_options()

        self.chosen_dir, self.chosen_words = self.get_answers()
        
        self.data = self.get_dir_data(self.chosen_dir)
        self.count_words(self.chosen_words, self.data)

        return
