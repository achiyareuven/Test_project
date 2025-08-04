from utils import load_data,write_to_Jason
from analysis.data_analyzer import DataAnalyzer
from cleaning.data_cleaner import DataCleaner

df = load_data(r"C:\Users\achiy\PycharmProjects\Test_project\data\tweets_dataset.csv")



a =DataAnalyzer(df)
a.amount_of_tweets()
a.average_words()
a.three_longest_tweets()
a.amount_of_uppercase()

s=(a.return_dict_result())

# write_to_Jason(s,r"C:\Users\achiy\PycharmProjects\Test_project\results\result.json")


clen=DataCleaner(df)

clen.update_to_lowercase()















