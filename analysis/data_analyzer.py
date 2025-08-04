import pandas as pd



class DataAnalyzer:
    def __init__(self, df):
        self.result = {}
        self.df = df

    # Number of tweets per category
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

    #Average words per tweet by category
    def average_words(self):
        self.df["word count"] = self.df["Text"].apply(lambda x:len(str(x).split()))
        antisemitic  = self.df[self.df["Biased"]==1]["word count"].mean()
        non_antisemitic  = self.df[self.df["Biased"]==0]["word count"].mean()
        total = self.df["word count"].mean()

        self.result["average_length"]={
             "antisemitic": antisemitic,
             "non_antisemitic": non_antisemitic,
             "total": total
        }

    # The three longest tweets
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
    #Number of words in uppercase letters by category
    def amount_of_uppercase(self):
        def count_uppercase_words(text):
            text = str(text)
            words = text.split()
            count =0
            for word in words:
                if word.isupper()and len(word)>1:
                    count +=1
            return count
        self.df["count uppercas"] = self.df["Text"].apply(count_uppercase_words)
        antisemitic = self.df[self.df["Biased"] == 1]["count uppercas"].sum()
        non_antisemitic = self.df[self.df["Biased"] == 0]["count uppercas"].sum()
        total = self.df["count uppercas"].sum()

        self.result["uppercase_words"] = {
            "antisemitic":antisemitic,
            "non_antisemitic":non_antisemitic,
            "total":total
        }

    #Returns a dictionary to write to JSON
    def return_dict_result(self):
        return self.result
