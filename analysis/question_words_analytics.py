import re


class QuestionWordsAnalytics:

    def __init__(self):
        self._word_for_quotes = ['повесть', 'сериал', 'фильм', 'сказк', 'картин', 'термин', 'псевдоним', 'книгу',
                                 'книга', 'выражение', 'группы', 'группа', 'программ', 'понятие', 'слово', 'стихотворен','роман']

    def first_word(self, q):
        return re.split("[ ,?\"«»“”.]", q)[0]

    def second_word(self, q):
        s = re.split("[ ,?\"«»“”.]", q)
        if len(s) < 2:
            return ""
        else:
            return s[1]

    def last_word(self, q):
        return re.split("[ ,?\"«»“”.]", q)[-1]

    def count_klever(self, q):
        return len(re.findall("клевер", q.lower()))

    def count_NE(self, q):
        return len(re.findall("НЕ", q))


    def count_NET(self, q):
        return len(re.findall("НЕТ", q))

    def has_what_is_quote(self, q):
        return int("Что такое «" in q)

    def uppercase_words_count(self, q):
        return len([x for x in re.split("[ ,?\"«»“”.]", q) if len(x) > 1 and x.isupper()])

    def uppercase_first_symbol_words_count(self, q):
        return len([x for x in re.split("[ ,?\"«»“”.]", q) if len(x) > 1 and x[0].isupper()])

    def words_count(self, q):
        return len([x for x in re.split("[ ,?\"«»“”.]", q) if len(x) > 1])

    def words_count_lat(self, q):
        pattern = re.compile("([a-zA-Z])")
        return len([x for x in re.split("[ ,?\"«»“”.]", q) if len(x) > 1 and pattern.search(x)])

    def first_symbol_uppercase(self, q):
        return int(q[0].isupper())

    def has_word_for_quotes(self, q):
        for w in self._word_for_quotes:
            if w in q:
                return 1
        return 0
