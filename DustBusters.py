import pandas 
"""pandas is used to read excel and CSV files, and convert them to SQL"""

def opening():
    print("""Welcome to DustBusters!
    We help beginner programmers gain experience and skills.
    They volunteer to work on old open-source projects, and we guide them how to refactor and dust outdated code.
    Workers and volunteers, please use this system to mark your attendance in DustBusters projects.""")

#create PIN and name dictionsry
excel_data = pandas.read_excel('add_data.xlsx', sheet_name='Sheet1')
num_list = excel_data['PIN'].tolist()
names_list = excel_data['Full Name'].tolist()
print(num_list)
print(names_list)

#dictionary comprehension

#given_num = input("Please enter your PIN: ")
#given_name = input("Please enter your full name: ")

