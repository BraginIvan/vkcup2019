import re
from collections import Counter


class WordCounterAnalytics():
    def __init__(self, df):

        the_text = ' '.join(df.Question.values).lower()
        split_text = re.split("[ ,?\"«»“”.]", the_text)
        self.counter = Counter(split_text)


    def _word_population(self, q, min_size):
        return [self.counter[x] for x in re.split("[ ,?\"«»“”.]", q.lower()) if len(x) >= min_size]

    def _word_population_dict(self, q, min_size):
        return {x:self.counter[x] for x in re.split("[ ,?\"«»“”.]", q.lower()) if len(x) >= min_size}


    def less_popular_word_count(self, q):
        wc = self._word_population(q, min_size=2)
        if len(wc) == 0:
            return 0
        return min(wc)

    def most_popular_word_count(self, q):
        wc = self._word_population(q, min_size=2)
        if len(wc) == 0:
            return 0
        return max(wc)

    def most_popular_word(self, q):
        wc = self._word_population_dict(q, min_size=2)
        word = ""
        count = 0
        for w,c in wc.items():
            if c > count:
                count = c
                word = w
        return word

    def first_popular_word(self, q):
        wc = self._word_population(q, min_size=1)
        if len(wc) == 0:
            return 0
        return wc[0]







