import pandas 
"""pandas"""

print ("""Welcome to DustBusters!
We help beginner programmers gain experience and skills.
They volunteer to work on old open-source projects,
and we guide them how to refactor and dust outdated code.
Workers and volunteers, please use this system to mark your attendance in DustBusters projects.""")

#create PIN and name dictionsry
PIN_name = pandas.read_excel('add_data.xlsx',
sheet_name='Sheet1', usecols = "A:B")

PIN_name_dictionary = PIN_name.to_dict()

print (PIN_name_dictionary)