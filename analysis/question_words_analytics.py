import re



class QuestionWordsAnalytics:

    def __init__(self):
        self._word_for_quotes = ['повесть', 'сериал', 'фильм', 'сказк', 'картин', 'термин', 'псевдоним', 'книгу',
                                 'книга', 'выражение', 'группы', 'группа', 'программ', 'понятие', 'слово', 'стихотворен','роман']

        self.cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань',
                       'Челябинск', 'Омск', 'Самара', 'Ростов-на-Дону', 'Уфа', 'Красноярск', 'Пермь', 'Воронеж', 'Волгоград', 'Краснодар']


        self.countries = ['Москва', 'Канада', 'Китай', 'США',  'Казахстан', 'Украина', 'Белорусия']

        self.splitter = "[\"”“„'.,+\\-*/ –()!\\\\:<>=|^’%—;…№#°@{}\\[\\]_$]"

        self.normal_upper_words=['НЕ', 'НЕТ', 'США', 'СССР', 'РФ']

    def has_city(self, q):
        for w in self.cities:
            if w in q:
                return 1
        return 0

    def has_lower_city(self, q):
        for w in self.cities:
            if w.lower() in q:
                return 1
        return 0

    def has_country(self, q):
        for w in self.countries:
            if w in q:
                return 1
        return 0

    def has_lower_country(self, q):
        for w in self.countries:
            if w.lower() in q:
                return 1
        return 0

    def max_word_len(self, q):
        return max([ len(i) for i in re.split(self.splitter, q)])

    def first_word(self, q):
        return re.split(self.splitter, q)[0]

    def first_word_len(self, q):
        return len(re.split(self.splitter, q)[0])


    def second_word(self, q):
        s = re.split(self.splitter, q)
        if len(s) < 2:
            return ""
        else:
            return s[1]

    def second_word_len(self, q):
        s = re.split(self.splitter, q)
        if len(s) < 2:
            return 0
        else:
            return len(s[1])

    def last_word(self, q):
        return re.split(self.splitter, q)[-1]

    def last_word_len(self, q):
        return len(re.split(self.splitter, q)[-1])

    def count_klever(self, q):
        return len(re.findall("клевер", q.lower()))

    def count_potter(self, q):
        return len(re.findall("поттер", q.lower()))

    def count_putin(self, q):
        return len(re.findall("путин", q.lower()))

    def count_sssr(self, q):
        return len(re.findall("ссср", q.lower()))

    def count_football(self, q):
        return len(re.findall("футбол", q.lower()))

    def count_means(self, q):
        return len(re.findall("называется", q.lower()))

    def count_means2(self, q):
        return len(re.findall("называют", q.lower()))


    def count_means3(self, q):
        return len(re.findall("зовут", q.lower()))

    def count_means4(self, q):
        return len(re.findall("название", q.lower()))


    def count_exists_word(self, q):
        return len(re.findall("существует", q.lower()))

    def count_2018_year(self, q):
        return len(re.findall("2018", q.lower()))

    def count_champ(self, q):
        return len(re.findall("чемпионат", q.lower()))



    def count_following_word(self, q):
        return len(re.findall("перечисленных", q.lower()))



    def count_city_word(self, q):
        return len(re.findall("город", q.lower()))


    def count_day(self, q):
        return len([x for x in re.split(self.splitter, q.lower()) if x == 'дней'])

    def count_years(self, q):
        return len([x for x in re.split(self.splitter, q.lower()) if x == 'году' or x == 'лет'])

    def count_what_is_upper(self, q):
        return len(re.findall("Что такое [A-ZА-Я]", q))

    def count_what_is_low(self, q):
        return len(re.findall("Что такое [a-zа-я]", q))

    def count_NE(self, q):
        return len(re.findall("НЕ", q))


    def count_NET(self, q):
        return len(re.findall("НЕТ", q))

    def has_what_is_quote(self, q):
        return int("Что такое «" in q)

    def uppercase_words_count(self, q):
        return len([x for x in re.split(self.splitter, q) if len(x) > 1 and x.isupper()])

    def uppercase_weird_words_count(self, q):
        return len([x for x in re.split(self.splitter, q) if len(x) > 1 and x.isupper() and x not in self.normal_upper_words])


    def uppercase_first_symbol_words_count(self, q):
        return len([x for x in re.split(self.splitter, q) if len(x) > 1 and x[0].isupper()])

    def words_count(self, q):
        return len([x for x in re.split(self.splitter, q) if len(x) > 1])

    def words_count_lat(self, q):
        pattern = re.compile("([a-zA-Z])")
        return len([x for x in re.split(self.splitter, q) if len(x) > 1 and pattern.search(x)])

    def has_lat_lower(self, q):
        pattern = re.compile("([a-zA-Z])")
        return len([x for x in re.split(self.splitter, q) if len(x) > 1 and pattern.search(x) and x[0].islower()])

    def first_symbol_uppercase(self, q):
        return int(q[0].isupper())

    def first_symbol_isalpha(self, q):
        return int(q[0].isalpha())

    def first_symbol_isdigit(self, q):
        return int(q[0].isdigit())

    def has_word_for_quotes(self, q):
        for w in self._word_for_quotes:
            if w in q.lower():
                return 1
        return 0
