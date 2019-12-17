
class QuestionBreakersAnalytics:

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

    def count_start_brackets_type1(self, q):  # no one
        return len([i for i in q if i == "("])

    def count_end_brackets_type1(self, q):  # no one
        return len([i for i in q if i == ")"])

    def is_balanced_brackets_type1(self, q):  # no one
        if not self.count_start_brackets_type1(q) == 0 and not self.count_end_brackets_type1(q) == 0:
            return -1
        return int(self._is_balanced(q, "(", ")"))

    def has_start_brackets_type2(self, q):  # no one
        return int("{" in q)

    def has_end_brackets_type2(self, q):  # no one
        return int("}" in q)

    def is_balanced_brackets_type2(self, q):  # no one
        if not self.has_start_brackets_type2(q) and not self.has_end_brackets_type2(q):
            return -1
        return int(self._is_balanced(q, "{", "}"))

    def has_brackets_type3(self, q):  # no one
        return int("<" in q) + int(">" in q)


    def is_balanced_brackets_type3(self, q):  # no one
        if self.has_brackets_type3(q) == 0:
            return -1
        return int(self._is_balanced(q, "<", ">"))

    def has_brackets_type4(self, q):  # no one
        return int("]" in q) + int("[" in q)




