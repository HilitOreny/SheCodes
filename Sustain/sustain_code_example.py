"""This module analyzes the content of an excel file for the Welcome Team of She Codes"""

import pandas
import datetime
import os


def pathfinder():
    path = '/python_scripts/welcome.xlsx'
    check_file_location = os.path.isfile(path)
    return check_file_location


def read_file(track_name):
    """This function opens a xlsx file and returns the content of the file. 
    :param track_name: The name of the track (the name of the sheet).
    :return: a dataframe which contains the content of the sheet in the excel file.
    """
    try:
        file_content = pandas.read_excel('/python_scripts/welcome.xlsx', sheet_name=track_name)
    except ImportError:
        print("Python tried to open the file, but encountered a problem. Contact code maintainers")
    except FileNotFoundError:
        print("The file is not present. Contact code maintainers")
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
    drop_unused = no_team.drop(columns=[
        "Index", "Staff", "Email", "Joined", "Track",
        "Attendance in the last 10 weeks", "Max Lesson Entered"])
    recent = drop_unused.drop(drop_unused.columns[[1, 2, 3, 4, 5, 6]], axis=1)
    return recent


def get_last_column(data):
    last_column_name = data.columns.values[-1]
    return last_column_name


def finished_track(all_students_df, last_column):
    all_lessons_completed = all_students_df[all_students_df[last_column] < 12]
    return all_lessons_completed


def remove_completed(data, last_column):
    """this function removes students who completed the 12 lesson from the dataframe.
    :return: a dataframe which contains only students who are in lesson 1 - 11"""
    still_learning = data[data[last_column] < 12]
    return still_learning


def missing_students(students_df, last_column):
    """this function filters the students who did not show up to the last lesson 
    return: a dataframe which contains only students who did not show up to the last lesson"""
    missed_last = students_df[students_df[last_column] == 0]
    return missed_last


def generate_excel(df_to_export, df_name, sheet_name):
    """this function generates an excel file with today's date and the dataframe's name.
    :param df_to_export: a dataframe to export to excel file. 
    :param df_name: dataframe's name to be copied to the excel file.
    :param sheet_name: the name of the excel sheet
    """
    today_string = datetime.datetime.today().strftime("%d %B, %Y")
    excel_name = f"{df_name} - {sheet_name} - {today_string}.xlsx"
    df_to_export.to_excel(excel_name)
    return


def file_analysis():
    track_list = ["Basic Python", "Python for Programmers", "React", "Web"]
    for item in track_list:
        excel_content = read_file(item)
        all_courses = generate_data(excel_content)
        last = get_last_column(all_courses)
        active_students = remove_completed(all_courses, last)
        missing = missing_students(active_students, last)
        generate_excel(missing, "missing students", item)


def getting_started():
    file_located = pathfinder()
    if file_located:
        file_analysis()
    else:
        message = """Please go to C folder and create a sub-folder called "python_scrips".
        Put welcome.xlsx in this folder"""
        print(message)


getting_started()
