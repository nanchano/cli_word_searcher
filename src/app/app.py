from os.path import isdir
from PyInquirer import prompt
from examples import custom_style_2
from counting.wordcounter import WordCounter
from filesystem_dicts.fsdicts import *

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

    LAST_QUESTION = [
        {
            'type': 'list',
            'name': 'final_options',
            'message': 'Select an option.',
            'choices': ['Search again', 'Change directory', 'Exit']
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

    def _eval_final_options(self):
        """Evaluates final options based on user input. Recursively runs the app again until exit choice."""
        ans = prompt(self.LAST_QUESTION, style=custom_style_2).get('final_options')
 
        if ans == 'Search again': 
            self.chosen_words = prompt(self.QUESTIONS[1], style=custom_style_2).get('words_choice').split()
            self.count_words(self.chosen_words, self.data)
            self._eval_final_options()

        elif ans == 'Change directory':
            self.chosen_dir, self.chosen_words = self.get_answers()
            self.data = self.get_dir_data(self.chosen_dir)
            self.count_words(self.chosen_words, self.data)
            self._eval_final_options()

        else:
            exit()

        return ans

    def get_answers(self) -> tuple:
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

        self._eval_final_options()

        return
