"""This module reads an excel file and formats it."""

import pandas


def read_file(track_name):
    """
    :param track_name: The name of the track, to be used as a sheet name.
    :return: a dataframe which contains the content of the Basic Python sheet in the excel file.
    """
    try:
        file_content = pandas.read_excel("Mock_Data.xlsx", sheet_name=track_name)
    except ImportError:
        print("Python tried to open the file, but encountered a problem. Contact code maintainers")
    else:
        return file_content


def generate_data(raw_excel_data):
    """this function replaces empty cells with 0 and removes irrelevant data.
    :param raw_excel_data: a dataframe which contains the raw data from the excel file.
    :unfiltered_data type: dataframe
    :return: a dataframe which only contains the relevant data.
    :rtype: dataframe"""
    filled_excel_data = raw_excel_data.fillna(0)
    no_team = filled_excel_data[filled_excel_data["Staff"] == "No"]
    drop = no_team.drop(columns=[
        "Index", "Staff", "Email", "Joined", "Track",
        "Attendance in the last 10 weeks", "Max Lesson Entered"])
    return drop


excel_content = read_file("React")
all_courses = generate_data(excel_content)
print(all_courses)
