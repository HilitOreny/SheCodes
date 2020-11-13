import pandas 
"""pandas is used to read the excel file, and convert it to SQL"""

excel_data = pandas.read_excel('Mock_Data.xlsx', sheet_name='Amazon')
names_list = excel_data['Name'].tolist()
membership_list = excel_data['Team Member'].tolist()
print(names_list)
print(membership_list)