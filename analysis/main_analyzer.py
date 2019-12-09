from analysis.work_counter_analytics import WordCounterAnalytics
from analysis.question_words_analytics import QuestionWordsAnalytics
from analysis.question_based_analytics import QuestionBasedAnalytics
from analysis.question_breakers_analytics import QuestionBreakersAnalytics
from analysis.question_quotes_analytics import QuestionQuotesAnalytics
from analysis.question_sign_analytics import QuestionSignAnalytics
from analysis.postprocess_question_analytics import PostprocessQuestionAnalytics
from analysis.postprocess_final_analytics import PostprocessFinalAnalytics
from analysis.utils import *


class MainAnalyzer:
    def __init__(self, data):
        self.word_counter_analytics = WordCounterAnalytics(data)
        self.question_words_analytics = QuestionWordsAnalytics()
        self.question_based_analytics = QuestionBasedAnalytics()
        self.question_breakers_analytics = QuestionBreakersAnalytics()
        self.question_quotes_analytics = QuestionQuotesAnalytics()
        self.question_sign_analytics = QuestionSignAnalytics()
        self.postprocess_question_analytics = PostprocessQuestionAnalytics()
        self.postprocess_final_analytics = PostprocessFinalAnalytics()

    def __call__(self, df):
        counter = {}
        order = []
        for q in df.Question.values:
            c = counter.get(q, 0)
            c = c + 1
            counter[q] = c
            order.append(c)

        df['order'] = order

        count = df.groupby(['Question'])['Question'].transform(lambda group: group.count())
        df['count']=count

        for q_base in [self.word_counter_analytics, self.question_words_analytics, self.question_based_analytics,
                       self.question_breakers_analytics, self.question_quotes_analytics, self.question_sign_analytics]:
            map_methods_from_class(df, q_base, 'Question')
        apply_methods_from_class(df, self.postprocess_question_analytics)
        apply_methods_from_class(df, self.postprocess_final_analytics)
