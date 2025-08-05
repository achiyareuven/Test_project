import  pandas as pd
import json

# Loads CSV to DF
def load_data(path):
    df = pd.read_csv(r"C:\Users\achiy\PycharmProjects\Test_project\data\tweets_dataset.csv")
    return df
#Writing the dictionary to a JSON file
def write_to_Jason(dict_result,file_path):
    try:
        with open(file_path,"w")as file:
            json.dump(dict_result,file)

    except Exception as e:
        print(f"error{e}")


def write_df_to_csv(df,file_path):
    try:
        df.to_csv(file_path,index=False)
    except Exception as e:
        print(f" error {e}")

