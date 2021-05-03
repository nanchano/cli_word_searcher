## Allows absolute imports outside main
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
print(package_root_directory)
sys.path.append(str(package_root_directory))
import unittest
from filesystem_dicts.file_dicts import *
from parsing.parser import Parser
from collections.abc import Iterable

class TestFileDict(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
        cls.path = '../../inputs/hamlet_TXT_FolgerShakespeare.txt' 
        cls.file_dict = FileDict(cls.path)

    def setUp(self):
        self.key = 'hamlet_TXT_FolgerShakespeare'
        self.value = 'hamlet_TXT_FolgerShakespeare.txt'

    def test__setitem__(self):
        self.file_dict[self.key] = self.value
        
        self.assertEqual(list(self.file_dict.keys())[0], self.key)
        self.assertEqual(list(self.file_dict.values())[0], Parser(self.path).parse())

    def test__getitem__(self):
        self.file_dict[self.key] = self.value
        self.assertEqual(self.file_dict[self.key], Parser(self.path).parse())

    def test__delitem__(self):
        self.file_dict[self.key] = self.value
        self.assertIs(self.file_dict.__delitem__(self.key), None)
        self.assertRaises(KeyError, self.file_dict.__getitem__, self.key)

    def test__len__(self):
        self.assertEqual(self.file_dict.__len__(), 1)
        self.file_dict['test_other_key'] = self.value
        self.assertEqual(self.file_dict.__len__(), 2)

    def test__iter__(self):
        self.file_dict[self.key] = self.value
        self.assertIsInstance(self.file_dict.__iter__(), Iterable)


class TestDirDict(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path = '../../inputs'
        cls.dir_dict = DirDict(cls.path)

    def test_get_files_from_dir(self):
        self.assertIsInstance(self.dir_dict.get_files_from_dir(), list)
        self.assertEqual(len(self.dir_dict.get_files_from_dir()), 42)

    def test_load_files(self):
        self.assertIsInstance(self.dir_dict.load_files(), dict)
        self.assertEqual(len(self.dir_dict.load_files()), 42)

if __name__ == '__main__':
    unittest.main()
