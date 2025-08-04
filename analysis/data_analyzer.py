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
        self.df["word count"] = self.df["Text"].apply(lambda x:len(str(x).split()))
        antisemitic  = self.df[self.df["Biased"]==1]["word count"].mean()
        non_antisemitic  = self.df[self.df["Biased"]==0]["word count"].mean()
        total = self.df[self.df["word count"]].mean()

        self.result["average_length"]={
             "antisemitic": antisemitic,
             "non_antisemitic": non_antisemitic,
             "total": total
        }
    def three_longest_tweets(self):
        self.df["word count"] = self.df["Text"].apply(lambda x:len(str(x).split()))

        antisemitic = (
            self.df[self.df["Biased"]==1]
            .sort_values(by="word count",ascending=False).head(3)["Text"].tolist()
        )
        non_antisemitic = (
            self.df[self.df["Biased"]==0]
            .sort_values(by="word count",ascending=False).head(3)["Text"].tolist()
        )
        self.result["longest_3_tweets"] = {
            "antisemitic":antisemitic,
            "non_antisemitic": non_antisemitic
        }

    def ten_common_words(self):
        pass

    def amount_of_uppercase(self):

        pass

    def return_dict_result(self):
        pass
