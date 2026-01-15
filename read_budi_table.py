from budilib import read_table_data

data = read_table_data()

# Print specific information about each table row
for element in data:
    print(element['given_name'],element['surname'])