import re
from collections import Counter
import numpy as np

class WordCounterAnalytics():
    def __init__(self, df):

        the_text = ' '.join(df[df.sure_is_bad==0].Question.values).lower()
        the_bad_text2 = ' '.join(df[df.sure_is_bad==1].Question.values).lower()

        self.full_splitter = "[ \"”“„'.,+\\-*/ –()!\\\\:<>=|^’%—;…№#°@{}\\[\\]_$]"
        self.splitter = "[ ,?«».]"

        split_text = re.split(self.splitter, the_text)
        split_bad_text = re.split(self.splitter, the_bad_text2)

        self.counter = Counter(split_text)
        self.bad_counter = Counter(split_bad_text)

    def _word_population(self, q, min_size):
        return [self.counter[x] for x in re.split(self.splitter, q.lower()) if len(x) >= min_size]

    def _word_population_dict(self, q, min_size):
        return {x: self.counter[x] for x in re.split(self.splitter, q.lower()) if len(x) >= min_size}


    def uppercase_less_popular_word_count(self, q):
        wc = [self.counter[x.lower()] for x in re.split(self.full_splitter, q) if x.isupper()]
        if len(wc) == 0:
            return 0
        return min(wc)

    def bad_words_percent(self, q):
        x1 = [self.counter[x] for x in re.split(self.splitter, q.lower()) if len(x) >= 2]
        x2 = [self.bad_counter[x] for x in re.split(self.splitter, q.lower()) if len(x) >= 2]
        if len(x2) >0:
            return np.mean(x2) / np.mean(x1)

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

    def word_after_quote_let(self, q):
        wc = re.split("[«»]", q.lower())
        if len(wc) == 1:
            return ""
        return len(re.split(self.full_splitter, wc[1]))

    def most_popular_word(self, q):
        wc = self._word_population_dict(q, min_size=2)
        word = ""
        count = 0
        for w, c in wc.items():
            if c > count:
                count = c
                word = w
        return word

    def most_popular_word_position(self, q):
        wc = self._word_population_dict(q, min_size=2)
        position = 0
        count = 0
        i=0
        for w, c in wc.items():
            i+=1
            if c > count:
                count = c
                position=i
        return position

    def less_popular_word_position(self, q):
        wc = self._word_population_dict(q, min_size=2)
        position = 0
        count = 1000
        i=0
        for w, c in wc.items():
            i+=1
            if c < count:
                count = c
                position = i
        return position

    def second_most_popular_word(self, q):
        wc = self._word_population_dict(q, min_size=2)
        second_word = ""
        second_word_count = 0
        word = ""
        count = 0
        for w, c in wc.items():
            if c > count:
                second_word = word
                second_word_count = count
                count = c
                word = w
            elif c > second_word_count:
                second_word = w
        return second_word

    def first_popular_word_count(self, q):
        wc = self._word_population(q, min_size=1)
        if len(wc) == 0:
            return 0
        return wc[0]

    def second_popular_word_count(self, q):
        wc = self._word_population(q, min_size=1)
        if len(wc) < 2:
            return 0
        return wc[1]

    def last_popular_word_count(self, q):
        wc = self._word_population(q, min_size=1)
        if len(wc) < 3:
            return 0
        return wc[-1]
