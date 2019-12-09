import re

class QuestionQuotesAnalytics:

    def _is_balanced(self, q, opening, closing):
        stack = []
        for character in q:
            if character in opening:
                stack.append(opening.index(character))
            elif character in closing:
                if stack and stack[-1] == closing.index(character):
                    stack.pop()
                else:
                    return False
        return not stack

    def count_start_quote_type1(self, q):
        return len([i for i in q if i == "«"])

    def count_end_quote_type1(self, q):
        return len([i for i in q if i == "»"])

    def is_balanced_quote_type1(self, q):
        if self.count_start_quote_type1(q) ==0 and self.count_end_quote_type1(q) == 0:
            return -1
        return int(self._is_balanced(q, "«", "»"))

    def count_start_quote_type3(self, q):  # no one
        return len([i for i in q if i == "“"])

    def count_end_quote_type3(self, q):  # no one
        return len([i for i in q if i == "”"])


    def is_balanced_quote_type3(self, q):
        if self.count_start_quote_type3(q)==0 and self.count_end_quote_type3(q)==0:
            return -1
        return int(self._is_balanced(q, "“", "”"))

    def quote_type2_count(self, q):
        return len([i for i in q if i == "\""])

    def is_balanced_quote_type2(self, q):
        if self.quote_type2_count(q) == 0:
            return -1
        return int((1+self.quote_type2_count(q)) % 2)

    def quote_type4_count(self, q):  # no one
        return len([i for i in q if i == "\'"])

    def is_balanced_quote_type4(self, q):
        if self.quote_type4_count(q) == 0:
            return -1
        return int((1+self.quote_type4_count(q)) % 2)

    def count_start_quote_type5(self, q):
        return len([i for i in q if i == "‘"])

    def count_end_quote_type5(self, q):
        return len([i for i in q if i == "’"])

    def is_balanced_quote_type5(self, q):
        if self.count_start_quote_type5(q)==0 and  self.count_end_quote_type5(q)==0:
            return -1
        return int(self._is_balanced(q, "‘", "’"))


    def has_quote_type4_noname_sign(self, q):  # no one
        pattern1 = re.compile("([^а-яА-Яa-zA-Z]')")
        pattern2 = re.compile("('[^а-яА-Яa-zA-Z])")
        if pattern1.search(q):
            return 1
        elif pattern2.search(q):
            return 1
        else:
            return 0

    def count_quote_type1_upper_symbol(self, q):  # no one
        pattern1 = re.compile("(«[А-ЯA-Z])")
        if pattern1.search(q):
            return 1
        else:
            return 0

    def count_quote_type1_lower_symbol(self, q):  # no one
        pattern1 = re.compile("(«[а-яa-z])")
        if pattern1.search(q):
            return 1
        else:
            return 0
