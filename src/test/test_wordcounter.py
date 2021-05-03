## Allows absolute imports outside main
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))
import unittest
from counting.wordcounter import WordCounter

class TestWordCounter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_words = ['shadows', 'mended', 'command']
        cls.counter = WordCounter(cls.test_words)

    def setUp(self):
        self.data1 = {'test1': 'shadows', 'test2': 'abcde', 'test3': 'mended'}
        self.data2 = {1: 1, 2: 2, 3: 3, 4: 4}

    def test_count(self):

        self.assertIsInstance(self.counter.count(self.data1), dict)

        counts1 = {'test1': 33, 'test2': 0, 'test3': 33} #1 / 3 * 100 = 33
        self.assertEqual(self.counter.count(self.data1), counts1)

        #type error cause values on data have to be subscriptables
        self.assertRaises(TypeError, self.counter.count, self.data2)

    def test_rank_top(self):
        counts = self.counter.count(self.data1)
        self.assertEqual(len(self.counter.rank_top(3)), 3)
        self.assertEqual(len(self.counter.rank_top(10)), 3) #checking no errors if topn > n_datapoints
        self.assertEqual(len(self.counter.rank_top(1)), 1)

    def test_print_top(self):
        counts = self.counter.count(self.data1)
        self.assertIs(self.counter.print_top(5), None)

    def test_simple_ratio(self):
        self.assertEqual(self.counter.simple_ratio(5, 5), 100)
        self.assertEqual(self.counter.simple_ratio(2, 3), 66)
        self.assertRaises(ZeroDivisionError, self.counter.simple_ratio, 100, 0)
        self.assertRaises(TypeError, self.counter.simple_ratio, 100, '100')

if __name__ == '__main__':
    unittest.main()

