import pandas 
"""pandas is used to read excel and CSV files, and convert them to SQL"""

import pyinputplus
"""this module provides more features for input validation"""


def opening():
    print("""Welcome to DustBusters!
    We help beginner programmers gain experience and skills.
    They volunteer to work on old open-source projects, and we guide them how to refactor and dust outdated code.
    Workers and volunteers, please use this system to mark your attendance in DustBusters projects.""")


def password_info(entire_df):
    """DO NOT use this function with real and sensitive data! It's here only for educational purposes.
    :param entire_df: a dataframe which contains the entire information of DustBusters' participants.
    :return: a dictionary of the participants names and their passwords"""
    num_list = entire_df['PIN'].tolist()
    names_list = entire_df['Full Name'].tolist()
    participants_dict = dict(zip(num_list, names_list))
    return participants_dict


def input_validation(passwords_names_dict):
    """
    :param passwords_names_dict: a dictionary of the participants names and their passwords
    :return: 
    """
    given_num = pyinputplus.inputInt(prompt="Please enter your PIN: ", blank=False)
    given_name = input("Please enter your full name: ")
    if given_num in passwords_names_dict.keys():
        print ("PIN found")
    if given_name in passwords_names_dict.values():
        print("Name found")

def run():
    """
    opens the file and applies the functions
    :return:
    """
    try:
        excel_content = pandas.read_excel('add_data.xlsx', sheet_name='Sheet1')
    except ImportError:
        print("Please install pandas and openpyxl modules in order to open the file")
    except OSError:
        print("Python could not open the file")
    else:
        passwords_dict = password_info(excel_content)
        input_validation(passwords_dict)


run()