import pandas as pd

class DataCleaner():
    def __init__(self,df):
        self.df = df
        self.df_resulte = None

    def remove_unclassified_rows(self):
        self.df = self.df([self.df["Biased"]]==0) | ([self.df["Biased"]]==1)

    def update_to_lowercase(self):
        self.df["Text"] =self.df["Text"].astype(str).apply(lambda x: x.lower())

    def remove_punctuation_marks(self):
        def clean_data(text):
            punctuation_marks = [".",",""?","!","_"]
            for punctuation in  punctuation_marks:
                text =str(text.replace(punctuation,""))
            return text

        self.df["Text"] = self.df["Text"].apply(clean_data)

    def get_cleaned_df(self):
        return self.df[["Text", "Biased"]]










#