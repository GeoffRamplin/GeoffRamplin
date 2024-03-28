import pandas as pd
# Reading the CSV file
data = pd.read_csv("Filtering_a_CSV_File\MOCK_DATA.csv")


# Function for filtering
def gender_filter(user_filter):
    new_gender = data[data[f"{user_selection}"].str.contains(f"{user_filter}", case=False)]
    print(new_gender)


# Introduction to the program
print("This is a data filtering tool with CSV files")
print("An example CSV file has been generated and written into this code.")
print("Please follow the prompts to filter and organise the data.")

while True:
    print("What data would you like to filter by?")
    header = data.columns
    for column in data.columns:
        print(column.title())
    user_selection = input("Please type the column name: ").lower()
    user_filter = input("Please type a minimum of 3 characters to filter by: ")
    gender_filter(user_filter)
