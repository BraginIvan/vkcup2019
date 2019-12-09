
class PostprocessFinalAnalytics:

    def sure_is_bad(self, df):
        return int((df.is_balanced_brackets_type1 == 0) | (df.has_comma_nospace == 1) | (df.has_next_line_sign > 0) | (
                df.has_wrong_quots == 1) | (df.end_with_question_condition == 0) | (df.first_symbol_uppercase == 0) | (
                           df.count_question_sign > 1) | (df.has_quote_type4_noname_sign ==1) | (df.is_balanced_quote_type1==0))



