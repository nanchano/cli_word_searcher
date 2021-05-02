import operator
from collections.abc import MutableMapping, Sequence

class WordCounter(object):

    def __init__(self, words: Sequence) -> None:
        self.words = set(words)
        self.total_words = len(self.words)
        self.counts = {}

    def count(self, data: MutableMapping) -> dict:
        for key, val in data.items():
            cnt = 0
            for word in self.words:
                if word in val:
                    cnt += 1
                    continue # one instance is enough, can continue with the rest of the words
            self.counts[key] = self.simple_ratio(cnt, self.total_words)

        return self.counts    

    def rank_top(self, n: int) -> dict:
        return dict(sorted(self.counts.items(), key=operator.itemgetter(1), reverse=True)[:n])

    def print_top(self, n: int) -> None:
        top_n = self.rank_top(n)

        for key, val in top_n.items():
            print(key, ': ', f'{val}%')

        return

    @staticmethod
    def simple_ratio(num, denom) -> int:
        return int(num/denom * 100)


        

