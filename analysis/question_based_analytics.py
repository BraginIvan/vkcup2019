import re

class QuestionBasedAnalytics:


    def count_dash(self, q):  # no one
        return len([i for i in q if i == "-"])

    def count_dash_no_space(self, q):  # no one
        pattern1 = re.compile("(-[\\s])")
        pattern2 = re.compile("([\\s]-)")
        if pattern1.search(q):
            return 0
        elif pattern2.search(q):
            return 0
        else:
            return 1


    def has_I_sign(self, q):  # no one
        return int("I" in q)


    def has_next_line_sign(self, q):  # no one
        return int("\\n" in q)

    def count_double_space(self, q):  # no one
        return len(re.findall("([\\s]{2})", q))


    def has_dot_nospace(self, q):
        pattern = re.compile("([^0-9]\.[а-яА-Яa-zA-Z])")
        if pattern.search(q):
            return 1
        else:
            return 0


    def has_comma_nospace(self, q):  # no one
        pattern = re.compile("([^0-9],[^\\s])")
        if pattern.search(q):
            return 1
        else:
            return 0

    def count_comma(self, q):
        return len([i for i in q if i == ","])

    def count_dot(self, q):
        return len([i for i in q if i == "."])


    def count_ellipsis(self, q):
        return len(re.findall("\.\.\.", q))

    def is_math(self, q):
        pattern = re.compile("([0-9][*\\-+/][0-9])")
        if pattern.search(q):
            return 1
        else:
            return 0

    def count_digit(self, q):
        return len(re.findall("[0-9]", q))

    def count_years(self, q):
        return len(re.findall("[0-9]{4}", q))

    def count_digitletter(self, q):
        return len(re.findall("[0-9][а-яa-z]", q.lower())) + len(re.findall("[а-яa-z][0-9]", q.lower()))

    def count_yo(self, q):
        return len(re.findall("ё", q.lower()))


    def has_name(self, q):
        pattern = re.compile("([А-Я]\\.[ ]{0,1}[А-Я]\\.[ ]{0,1}[А-Я])")
        if pattern.search(q):
            return 1
        else:
            return 0

    def count_weird_signs(self, q):
        return len(re.findall("[\"”“„'.,+\\-*/ –()!\\\\:<>=|^’%—;…№#°@{}\\[\\]_$]", q)) #^0-9a-zа-яA-ZА-ЯёЁ?«»

    def count_consonants_ssigns(self, q):
        return len(re.findall("[бвгджзклмнпрстфхцчшщ]", q))

    def count_vowels_signs(self, q):
        return len(re.findall("[ауоыиэяюёе]", q))

    def count_signs(self, q):
        return len(q)



