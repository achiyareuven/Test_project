from utils import load_data,write_to_Jason,write_df_to_csv
from analysis.data_analyzer import DataAnalyzer
from cleaning.data_cleaner import DataCleaner

def run_all():
    df = load_data(r"C:\Users\achiy\PycharmProjects\Test_project\data\tweets_dataset.csv")
    analysis = DataAnalyzer(df)
    analysis.full_analysis()
    print("analysis completed")
    dict_result= analysis.return_dict_result()
    print( dict_result)
    write_to_Jason(dict_result,r"C:\Users\achiy\PycharmProjects\Test_project\results\result.json")

    cleaner = DataCleaner(df)
    cleaner.full_cleaning()
    cleaned_df = cleaner.get_cleaned_df()
    write_df_to_csv(cleaned_df,r"C:\Users\achiy\PycharmProjects\Test_project\results\cleaned_dataset_tweets.csv")


# analysis =None
# cleaned_df = None
#
# def run():
#     global analysis,cleaned_df
#     while True:
#         print("""
#         1. For analyzing data from CSV
#         2. Clear the data
#         3. to print the analysis
#         4. To write the analysis to a file
#         0. Exit
#         """)
#         choice = input("choose option: ").strip()
#         if choice == "1":
#             path_user = input("enter a path to CSV file for data analysis: ")
#             df = load_data(path_user)
#             analysis =DataAnalyzer(df)
#             analysis.full_analysis()
#             print("analysis completed")
#
#         elif choice == "2":
#             path_user = input("enter a path to CSV file for data analysis: ")
#             df = load_data(path_user)
#             cleaner = DataCleaner(df)
#             cleaner.full_cleaning()
#             cleaned_df = cleaner.get_cleaned_df()
#             write_df_to_csv(cleaned_df,path_user)
#
#         elif choice == "3":
#             pass
#         elif choice == "4":
#             pass
#         elif choice == "0":
#             break
#         else:
