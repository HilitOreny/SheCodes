import pandas 
"""pandas is used to read the excel file and analyze the data"""

def generate_data():
    """this function reads the excel file and formats it by replacing empty cells with 0 and removing irrelevant data.
    :return: a dataframe which only contains the relevant data.
    :rtype: dataframe"""
    raw_excel_data = pandas.read_excel("Mock_Data.xlsx", sheet_name="Amazon")
    filled_excel_data = raw_excel_data.fillna(0)
    drop_branch_name = filled_excel_data.drop(columns=["Branch"])
    no_team = drop_branch_name[drop_branch_name["Team Member"] == "No"]
    drop_team = no_team.drop(columns=["Team Member"])
    no_final_project = drop_team[drop_team["Course"] != "Final Project"]
    return no_final_project

def final_lesson_iteration(sample_df):
    """
    """
    check_final_lesson = sample_df.eq(13)
    omit_final_lesson = check_final_lesson
    return 
    



all_courses = generate_data()
basic_python_raw = all_courses[all_courses["Course"] == "Basic Python"]
basic_python_filtered = basic_python_raw.drop(columns=["Course"])
web_raw = all_courses[all_courses["Course"] == "Web"]
web_filtered = web_raw.drop(columns=["Course"])
react_raw = all_courses[all_courses["Course"] == "React"]
react_filtered = react_raw.drop(columns=["Course"])
advanced_python_raw = all_courses[all_courses["Course"] == "Python for Programmers"]
advanced_python_filtered = advanced_python_raw.drop(columns=["Course"])
