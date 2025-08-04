import  pandas as pd


def load_data(path):
    df = pd.read_csv(r"C:\Users\achiy\PycharmProjects\Test_project\data\tweets_dataset.csv")
    return df