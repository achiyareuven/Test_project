from utils import load_data
from analysis.data_analyzer import DataAnalyzer

df = load_data(r"C:\Users\achiy\PycharmProjects\Test_project\data\tweets_dataset.csv")
# print(a.shape)
a = df.groupby("Biased")["Text"].count
print(a)





# print(df.value_counts("Biased"))
# count_mising_val = df.isnull().sum()
# print(count_mising_val)
# a= (df['Biased'].unique())
# print(a)
# for val in a :
#     if val == 1:
#         print(df.value_counts("Biased")[0])
#     elif val == 0 :
#         print(df.value_counts("Biased")[1])

d = DataAnalyzer(df)

