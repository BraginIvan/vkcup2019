import re


class QuestionSignAnalytics:

    def count_question_sign(self, q):  # only 7953
        return len([i for i in q if i == "?"])

    def ends_with_question_sign(self, q):  # only 7953
        return int(q.endswith("?"))

    def ends_with_question_sign_space(self, q):
        return int(q.endswith("? "))

    def ends_with_space_question_sign(self, q):
        return int(q.endswith(" ?"))

    def ends_with_quote_space_question_sign(self, q):
        return int(q.endswith("» ?"))

    def ends_with_question_sign_quote_type1(self, q):
        return int(q.endswith("?»"))

    def has_space_question_sign(self, q):  # no one
        pattern = re.compile("([\\s]\\?)")
        if pattern.search(q):
            return 1
        else:
            return 0

    def has_nonletter_question_sign(self, q):  # no one
        pattern = re.compile("([^a-zа-я]\\?)")
        if pattern.search(q.lower()):
            return 1
        else:
            return 0

