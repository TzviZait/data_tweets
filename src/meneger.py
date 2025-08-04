from read_data_csv import Data_analysis

class Meneger:

    @staticmethod
    def meneger():
        dic = {"total_tweets":
                {
                   "antisemitic":Data_analysis.sum_tweets_1(),
                    "non_antisemitic":Data_analysis.sum_tweets_0(),
                    "total":Data_analysis.sum_tweets()
                },
                "average_length":
                {
                    "antisemitic":Data_analysis.average_1_tweets(),
                    "non_antisemitic":Data_analysis.average_0_tweets(),
                    "total":Data_analysis.average_all_tweets()
                },
                "common_words":
                {
                    "total":Data_analysis.common_words()
                },
                "longest_3_tweets":
                {
                    "antisemitic":Data_analysis.lengest_tweets_1(),
                    "non_antisemitic":Data_analysis.lengest_tweets_0()
                },
                "uppercase_words":
                {
                    "antisemitic":Data_analysis.uppercase_words_1(),
                    "non_antisemitic":Data_analysis.uppercase_words_0(),
                    "total":Data_analysis.uppercase_words_total()
                }
              }
        return dic

