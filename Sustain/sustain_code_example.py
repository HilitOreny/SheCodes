import pandas

"""pandas is used to read the excel file and analyze the data"""


def read_file():
    """
    :return: a dataframe which contains the content of the excel file.
    """
    try:
        file_content = pandas.read_excel("Mock_Data.xlsx", sheet_name="Amazon")
    except ImportError:
        print("Python tried to open the file, but encountered a problem. Contact code maintainers")
    else:
        return file_content


def generate_data(raw_excel_data):
    """this function reads the excel file and formats it by replacing empty cells with 0 and removing irrelevant data.
    :param raw_excel_data: a dataframe which contains the raw data from the excel file.
    :unfiltered_data type: dataframe
    :return: a dataframe which only contains the relevant data.
    :rtype: dataframe"""
    filled_excel_data = raw_excel_data.fillna(0)
    no_team = filled_excel_data[filled_excel_data["Team Member"] == "No"]
    remove_final_project = no_team[no_team["Course"] != "Final Project"]
    drop_branch_name = remove_final_project.drop(columns=["Branch", "Team Member"])
    return drop_branch_name

#TO DO: 13

def inner_course_filtering(general_df, course_name):
    """this function filters the data of a specific course to find struggling students.
    :param general_df: a dataframe of all courses
    :type general_df: dataframe
    :param course_name: the name of the course to be filtered.
    :type course_name: str
    :return:
    """
    raw = general_df[general_df["Course"] == course_name]
    filtered_data = raw.drop(columns=["Course"])
    for index, row in filtered_data.iterrows():
        listed = list(row)
        if 13.0 in listed:
            listed.clear()
    return filtered_data


excel_content = read_file()
all_courses = generate_data(excel_content)
basic_python = inner_course_filtering(all_courses, "Basic Python")
web = inner_course_filtering(all_courses, "Web")
print(web)
react = inner_course_filtering(all_courses, "React")
advanced_python = inner_course_filtering(all_courses, "Python for Programmers")
