# 🎓 Student Details Extractor 📄

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pandas](https://img.shields.io/badge/Library-Pandas-green)
![Automation](https://img.shields.io/badge/Automation-Excel%20to%20TXT-yellow)

## 📜 Project Overview
**Ever had a bunch of student details from Google Forms and needed to organize them neatly?** Instead of getting lost in the maze of spreadsheets, this project automates the task of extracting individual student data and creating custom `.txt` files. Each student gets their very own file, so you can access their info in an instant!

### ✨ What Does It Do?
- 🎯 **Reads an Excel file** with student info (from Google Form submissions or any other source).
- ✂️ **Extracts key details**: Name, Department, DOB, College, Mobile Number, CGPA, and Skills.
- 📂 **Generates individual `.txt` files** for each student, named after the student (e.g., `Darshan.txt`).
- 🔄 **Automation** at its best! Less manual work, more efficiency.

---

## 🚀 Quick Start Guide

### 💻 Installation

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/student-details-extractor.git
   cd student-details-extractor
   ```

2. **Install the necessary dependencies**:
   ```bash
   pip install pandas openpyxl
   ```

3. **Prepare your Excel file**:
   - Make sure your Excel file (e.g., `Info.xlsx`) contains the following columns:
     - `Name`, `Department`, `DOB`, `College Name`, `Mobile Number`, `CGPA`, `Technical Skills`.
   - If the column names differ, feel free to modify the script to match your column names.

4. **Place the Excel file in the root directory** of the project.

---

### 🛠️ Usage Instructions

1. Open your terminal/command prompt and **navigate to the project folder**:
   ```bash
   cd path/to/student-details-extractor
   ```

2. **Run the script** and let the magic happen:
   ```bash
   python extract_student_details.py
   ```

3. **Watch the magic unfold**! You’ll find a new folder called `student_details` filled with `.txt` files, each named after a student. Each file contains their personal info extracted from the Excel sheet.

---

### 🎉 Example Output (`darshan.txt`):
```
Name: Darshan
Department: Computer Science
Date of Birth: 2000-05-14
College Name: ABC College
Mobile Number: 9876543210
CGPA: 8.5
Skills: Python, Java, HTML
```

---

## 💡 Why You’ll Love This Project

- **No more sifting through endless rows of data**! It’s quick, automated, and super easy.
- Perfect for **universities, event organizers**, or anyone who needs to manage student data in bulk.
- Simple to **customize** – want to include more info or change the format? Modify the script in seconds!

---

## 🛠️ Customization Tips
- Not happy with the column names in the Excel sheet? No problem! Just update the script.
- Want to change the format of the `.txt` file? The file generation is as flexible as you need.

Example, if your Excel sheet has `Dept` instead of `Department`:
```python
department = row['Dept']  # Update to match your Excel column
```

---

## 🌟 Why Contribute?

Got ideas for cool features? Think this project could benefit others? **Contribute**! Add more functionalities, optimize the script, or even give it a cool new output format. Contributions are always welcome!

---

## 📝 License

This project is licensed under the **MIT License**. For more details, see the [LICENSE](LICENSE) file.

---

## 📧 Get in Touch

Have questions or need support? Reach out at [your-email@example.com](mailto:your-email@example.com).
