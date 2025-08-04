import pandas as pd

class Data_analysis:

    @staticmethod
    def read_data_csv():
        data = pd.read_csv("../data/tweets_dataset.csv")
        return data

    @staticmethod
    def sum_tweets_0():
        data = Data_analysis.read_data_csv()
        mask0 = data["Biased"] == 0
        sum_0 = len(data[mask0])
        return sum_0

    @staticmethod
    def sum_tweets_1():
        data = Data_analysis.read_data_csv()
        mask1 = data["Biased"] == 1
        sum_1 = len(data[mask1])
        return sum_1

    @staticmethod
    def sum_tweets():
        data = Data_analysis.read_data_csv()
        sum_all = len(data["Biased"])
        return sum_all

    @staticmethod
    def average_all_tweets():
        data = Data_analysis.read_data_csv()
        avg = data["Text"].str. split().apply(len).mean()
        return avg

    @staticmethod
    def average_0_tweets():
        data = Data_analysis.read_data_csv()
        mesk0 = data["Biased"] == 0
        data0 = data[mesk0]
        avg0 = data0["Text"].str.split().apply(len).mean()
        return avg0

    @staticmethod
    def average_1_tweets():
        data = Data_analysis.read_data_csv()
        mesk1 = data["Biased"] == 1
        data1 = data[mesk1]
        avg1 = data1["Text"].str.split().apply(len).mean()
        return avg1

    @staticmethod
    def lengest_tweets_0():
        data = Data_analysis.read_data_csv()
        data["len"] = data["Text"].str.len()
        mesk0 = data["Biased"] == 0
        data0 = data[mesk0]
        data0 = data0.nlargest(3, "len")["Text"].values
        return data0

    @staticmethod
    def lengest_tweets_1():
        data = Data_analysis.read_data_csv()
        data["len"] = data["Text"].str.len()
        mesk1 = data["Biased"] == 1
        data1 = data[mesk1]
        data1 = data1.nlargest(3, "len")["Text"].values
        return data1

    @staticmethod
    def common_words():
        data = Data_analysis.read_data_csv()
        dic = {}
        for i in data["Text"]:
            i = i.split()
            for j in i:
                if j not in dic:
                    dic[j] = 1
                if j in dic:
                    dic[j] += 1
        dic = sorted(dic.items(), key=lambda x: x[1],reverse=True)[:10]
        dic = [key for key,value in dic]
        return dic

    @staticmethod
    def uppercase_words_total():
        data = Data_analysis.read_data_csv()
        sum_upper = 0
        for i in data["Text"]:
            i = i.split()
            for j in i:
                if j.isupper():
                    sum_upper += 1
        return sum_upper

    @staticmethod
    def uppercase_words_0():
        data = Data_analysis.read_data_csv()
        sum_upper = 0
        mesk0 = data["Biased"] == 0
        data0 = data[mesk0]
        for i in data0["Text"]:
            i = i.split()
            for j in i:
                if j.isupper():
                    sum_upper += 1
        return sum_upper

    @staticmethod
    def uppercase_words_1():
        data = Data_analysis.read_data_csv()
        sum_upper = 0
        mesk1 = data["Biased"] == 1
        data1 = data[mesk1]
        for i in data1["Text"]:
            i = i.split()
            for j in i:
                if j.isupper():
                    sum_upper += 1
        return sum_upper



print(Data_analysis.uppercase_words_1())
print(Data_analysis.uppercase_words_0())
print(Data_analysis.uppercase_words_total())

