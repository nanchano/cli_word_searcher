## Allows absolute imports outside main
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))
import unittest
from parsing.parser import Parser

class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser_valid = Parser('../../inputs/hamlet_TXT_FolgerShakespeare.txt') #valid input
        cls.parser_invalid = Parser('../../inputs/wrong_file.txt') #invalid input, file doesnt exist

    def setUp(self):
        pass

    def test_parse(self):
        self.data_valid = self.parser_valid.parse()
        self.assertIs(type(self.data_valid), set)
        self.assertRaises(FileNotFoundError, self.parser_invalid.parse)


    def test_write(self):
        self.assertIs(self.parser_valid.write('./output/valid_data.txt'), None)

    def test_file_exists(self):
        self.assertTrue(self.parser_valid._file_exists('test_parser.py'))
        self.assertFalse(self.parser_valid._file_exists('wrong_file.py'))

    def test_dir_exists(self):
        self.assertTrue(self.parser_valid._dir_exists('../test/'))
        self.assertFalse(self.parser_valid._dir_exists('../wrong_dir/'))

if __name__ == '__main__':
    unittest.main()
