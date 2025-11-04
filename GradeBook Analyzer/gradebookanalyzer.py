# GradeBook Analyzer
# Sushant
# 2501350065
# B.Tech CSE (FSD)
# 01/11/2025

import csv

# input data

def manual_entry():
    marks = {}
    print("Enter student details (Press enter to stop):")
    while True:
        name = input("Enter student name: ---> ")
        if name == "":
            break
        score = float(input("Enter marks:---> "))
        marks[name] = score
    return marks
    
def load_csv():
    marks = {}
    filename = input("Enter CSV file name: --->  ")
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != "Name":
                    marks[row[0]] = float(row[1])
    except:
        print("File not found, wrong file name entered.")
    return marks

# calculations
def avg(marks):
    total = sum(marks.values())
    count = len(marks)
    return total / count

def median(marks):
    values = sorted(marks.values())
    n = len(values)
    if n % 2 == 1:
        return values[n // 2]
    else:
        return (values[n // 2 - 1] + values[n // 2]) / 2


def max_score(marks):
    name = max(marks, key=marks.get)
    return name, marks[name]

def min_score(marks):
    name = min(marks, key=marks.get)
    return name, marks[name]

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
    
# display

def show_results(marks):
    print("\n-------- Results -------")
    print("Name\tMarks\tGrade")
    print("------------------------")
    
    grades = {}
    
    for name, score in marks.items():
        grade = assign_grade(score)
        grades[name] = grade
        print(f"{name}\t{score}\t{grade}")
        
# grade count
    grade_count = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for g in grades.values():
        grade_count[g] += 1

# pass / fail
    passed = [name for name, s in marks.items() if s >= 40]
    failed = [name for name, s in marks.items() if s < 40]

# stats
    print("\nAverage Marks:", avg(marks))
    print("\nMedian Marks:", median(marks))
    high_name, high_score = max_score(marks)
    low_name, low_score = min_score(marks)
    print("\nHighest marks:---> ", high_name , ("<--->") , high_score)
    print("\nLowest marks:---> ", low_name , ("<--->") , low_score)

    print("\nGrade Count:")
    print(grade_count)

    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

# main menue
marks = {}
while True:
    print("========== Menu ==========")
    print("1. Want To Enter Marks Manually")
    print("2. Load From CSV File")
    print("3. Show Results")
    print("4. Exit")
    
    choice = input("Enter choice: ---> ")
    if choice == "1":
        marks = manual_entry()
    elif choice == "2":
        marks = load_csv()
    elif choice == "3":
        if marks:
            show_results(marks)
        else:
            print("No data entered yet!")
    elif choice == "4":
        print("THANK YOU FOR USING ME")
        break
    else:
        print("Invalid choice , choose correct option.")
