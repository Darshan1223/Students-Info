import pandas as pd
import os

# Load the Excel file that contains the Google Form submissions
input_file = "Info.xlsx"  # Path to your Excel file with form submissions
output_folder = "student_details"  # Folder to store individual .txt files

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(input_file)

# Iterate through each row (i.e., each student's details)
for index, row in df.iterrows():
    # Extract student's details
    name = row['Name']
    email_id = row['Email Id']
    dept = row['Department']
    dob = row['Date of Birth']
    college_name = row['College Name']
    mobile_number = row['Mobile No']
    cgpa = row['CGPA']
    skills = row['Skills']

    # Prepare the content for the .txt file
    student_details = f"""
    Name: {name}
    email Id: {email_id}
    Department: {dept}
    Date of Birth: {dob}
    College Name: {college_name}
    Mobile Number: {mobile_number}
    CGPA: {cgpa}
    Skills: {skills}
    """

    # Define the output file path (e.g., darshan.txt for student "Darshan")
    output_file_path = os.path.join(output_folder, f"{name}.txt")

    # Write the student's details into the .txt file
    with open(output_file_path, "w") as file:
        file.write(student_details)

print("All student details have been stored in individual text files.")
