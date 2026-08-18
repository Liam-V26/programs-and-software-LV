# =================================================================================================================================================================
# Create a python program that gets a user's name and surname. Then ask them their age. subtract their age from a variable named current-year with a value 2026.
# Display their full name and year of birth
#==========================================================
#variables?   1. name => user input <= int
#             2. surname=> user input <= int
#             3. age => user input <= int
#             4. current year => 2026 <= int
#             5. year_of_birth => current_year-age
#             6. full_name => name+""+surname
# =================================================================================================================================================================
#imports
import csv
import os

current_year = 2026
people_list = []  # a Empty list to store everyone's data

while True:
    # 1 Get name
    while True:
        name = input("\nPlease enter your name: ").strip()
        if name.isalpha():
            break
        print("Invalid name. Please use letters only and do not leave it blank.")
    print("-" * 20)
    # 2 Get surname
    while True:
        surname = input("Please enter your surname: ").strip()
        if surname.replace(" ", "").isalpha():
            break
        print("Invalid surname. Please use letters only and do not leave it blank.")
    print("-" * 20)
    # 3 Get age
    while True:
        age_input = input("Enter your age: ").strip()
        if age_input.isdigit():
            age = int(age_input)
            break
        print("Invalid age. Please enter a valid number.")
    print("-" * 20)
    # Calculations
    year_of_birth = current_year - age
    full_name = name + " " + surname

    # Dictionary for the current person
    person_data = {
        "full_name": full_name,
        "year_of_birth": year_of_birth
    }
    
    # Save this person to master list
    people_list.append(person_data)

    # Asking if you want to continu or stop
    while True:
        choice = input("\nDo you want to add another person? (yes/no): ").strip().lower()
        if choice in ['yes', 'no', 'y', 'n']:
            break
        print("Invalid choice. Please type 'yes' or 'no'.")
    
    # If they said no break the outer loop to stop collecting data
    if choice in ['no', 'n']:
        break

# Summery display 
print("\n" + "=" * 30)
print(f"SUMMARY: {len(people_list)} PEOPLE ADDED")
print("=" * 30)

for person in people_list:
    print(f"Full Name:     {person['full_name']}")
    print(f"Year of Birth: {person['year_of_birth']}")
    print("-" * 30)

folder_path = r"C:\Users\liamv\Desktop\Desktop\MyPython projects\Data"
filename = os.path.join(folder_path, "people_data.csv")

# This will create a folder if one does not exist 
os.makedirs(folder_path, exist_ok=True)

# 'w' will create the people_data.csv file
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["full_name", "year_of_birth"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(people_list)
         
print(f"Successfully saved to '{filename}'!")