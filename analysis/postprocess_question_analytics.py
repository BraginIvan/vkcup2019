
class PostprocessQuestionAnalytics:

    def end_with_question_condition(self, df):
        return int((df.ends_with_question_sign == 1) | (df.ends_with_question_sign_space == 1) | (
                    df.ends_with_question_sign_quote_type1 == 1))

    def has_wrong_quots(self, df):
        return int((df.quote_type2_count > 0) | (df.count_start_quote_type3 > 0) | (
                    df.count_end_quote_type3 > 0))





