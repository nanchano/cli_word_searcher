## Allows absolute imports outside main
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
print(package_root_directory)
sys.path.append(str(package_root_directory))
import unittest
from unittest.mock import patch
from app.app import App

class TestApp(unittest.TestCase):
    ## get_dir_data and count_words tested on test_fsdicts and test_wordcounter respectively
    
    @classmethod
    def setUpClass(cls):
        cls.app = App()

    @patch('app.app.prompt', return_value={'start_options': 'Exit'})
    def test_eval_start_exit(self, mock_prompt):
        self.assertRaises(SystemExit, self.app._eval_start_options)
 
    @patch('app.app.prompt', return_value={'start_options': 'Help'})
    def test_eval_start_help(self, mock_prompt):
        self.assertIs(self.app._eval_start_options(), None)

    @patch('app.app.prompt', return_value={'start_options': 'Anythingelse'})
    def test_eval_start_search(self, mock_prompt):
        self.assertIs(self.app._eval_start_options(), None)

    @patch('app.app.prompt', return_value={'directory_choice': '../../inputs/', 'words_choice': 'shadows'})
    def test_get_answers(self, mock_prompt):
        self.assertIsInstance(self.app.get_answers(), tuple)
        self.assertEqual(self.app.get_answers(), ('../../inputs/', ['shadows'])) #we transform words into list in the app

    @patch('app.app.prompt', return_value={'final_options': 'Exit'})
    def test_eval_final_exit(self, mock_prompt):
        self.assertRaises(SystemExit, self.app._eval_final_options)


if __name__ == '__main__':
    unittest.main()
