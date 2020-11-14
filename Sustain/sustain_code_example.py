import pandas

"""pandas is used to read the excel file and analyze the data"""


def read_file():
    """
    :return: a dataframe which contains the content of the excel file.
    """
    try:
        raw_excel_data = pandas.read_excel("Mock_Data.xlsx", sheet_name="Amazon")
    except ImportError:
        print("Python tried to open the file, but encountered a problem. Contact code maintainers")
    else:
        return raw_excel_data


def generate_data(unfiltered_data):
    """this function reads the excel file and formats it by replacing empty cells with 0 and removing irrelevant data.
    :param unfiltered_data: a dataframe which contains the raw data from the excel file.
    :unfiltered_data type: dataframe
    :return: a dataframe which only contains the relevant data.
    :rtype: dataframe"""
    filled_excel_data = unfiltered_data.fillna(0)
    drop_branch_name = filled_excel_data.drop(columns=["Branch"])
    no_team = drop_branch_name[drop_branch_name["Team Member"] == "No"]
    drop_team = no_team.drop(columns=["Team Member"])
    no_final_project = drop_team[drop_team["Course"] != "Final Project"]
    return no_final_project


file_content = read_file()
all_courses = generate_data(file_content)
basic_python_raw = all_courses[all_courses["Course"] == "Basic Python"]
basic_python_filtered = basic_python_raw.drop(columns=["Course"])
web_raw = all_courses[all_courses["Course"] == "Web"]
web_filtered = web_raw.drop(columns=["Course"])
react_raw = all_courses[all_courses["Course"] == "React"]
react_filtered = react_raw.drop(columns=["Course"])
advanced_python_raw = all_courses[all_courses["Course"] == "Python for Programmers"]
advanced_python_filtered = advanced_python_raw.drop(columns=["Course"])

print(basic_python_filtered)
print (web_filtered)
print(react_filtered)
print(advanced_python_filtered)
