import pandas

"""pandas is used to read the excel file and analyze the data"""


def read_file_basic_python():
    """
    :return: a dataframe which contains the content of the Basic Python sheet in the excel file.
    """
    try:
        file_content = pandas.read_excel("Mock_Data.xlsx", sheet_name="Basic Python")
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
    no_team = filled_excel_data[filled_excel_data["Staff"] == "No"]
    drop = no_team.drop(columns=[
        "Index", "Staff", "Email", "Joined", "Track", "Attendance in the last 10 weeks", "Max Lesson Entered"])
    return drop

excel_content = read_file_basic_python()
all_courses = generate_data(excel_content)
print (all_courses)