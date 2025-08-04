import pandas as pd


class DataAnalyzer:
    def __init__(self, df):
        self.result = {}
        self.df = df

    def amount_of_tweets(self):
        antisemitic = 0
        non_antisemitic = 0
        total = 0
        unspecified = 0
        for index, row in self.df.iterrows():
            if row["Biased"] == 1:
                antisemitic += 1
            elif row["Biased"] == 0:
                non_antisemitic +=1
            else:
                unspecified +=1
        total = antisemitic  + non_antisemitic +unspecified

        self.result["total_tweets"]={
            "antisemitic":antisemitic,
            "non_antisemitic":non_antisemitic,
            "total":total,
            "unspecified":unspecified
        }


    def average_words(self):
        self.df["word count"] = self.df[self.df]["Text"].apply(lambda x:len(x.split()))
        antisemitic  = self.df[self.df["Biased"]]=1["Text"].mean
        non_antisemitic  = self.df[self.df["Biased"]]=0["Text"].mean
        total = self.df[self.df["Text"]].mean

        self.result["average_length"]={
             "antisemitic": antisemitic,
             "non_antisemitic": non_antisemitic,
             "total": total
        }


    def ten_common_words(self):
        pass

    def amount_of_uppercase(self):
        pass

    def return_dict_result(self):
        pass
