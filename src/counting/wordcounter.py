import operator
from collections.abc import MutableMapping, Sequence

class WordCounter(object):
    """Counts instances of given words inside a set of data."""
    def __init__(self, words: Sequence) -> None:
        """Initializes the class.
        Args:
            words (Sequence): iterable of words to search."""
        self.words = set(words)
        self.total_words = len(self.words)
        self.counts = {}

    def count(self, data: MutableMapping) -> dict:
        """Counts instances of each word for each data point.
        Args:
            data (MutableMapping): dict-type object that represents the data.
        Returns:
            dict
        """
        for key, val in data.items():
            cnt = 0
            for word in self.words:
                if word in val:
                    cnt += 1
                continue # one instance is enough, can continue with the rest of the words
            self.counts[key] = self.simple_ratio(cnt, self.total_words)

        return self.counts    

    def rank_top(self, n: int) -> dict:
        """Gives top n of word counts on the data
        Args: 
            n (int): number of elements on the top list
        Returns:
            dict
        """
        return dict(sorted(self.counts.items(), key=operator.itemgetter(1), reverse=True)[:n])

    def print_top(self, n: int) -> None:
        """Prints the top n
        Args:
            n (int): number of elements on the top list
        """
        top_n = self.rank_top(n)

        for key, val in top_n.items():
            print(key, ': ', f'{val}%')

        return

    @staticmethod
    def simple_ratio(num: int, denom: int) -> int:
        """Simple equation to normalize and calculate the instances of all words on the data
        Args:
            num (int): numerator
            denom (int): denominator
        Returns:
            int    
        """
        return int(num/denom * 100)


        

