# This is the Blueprint for this assignment.
from typing import Any


class Assignment: 
    def __init__(self, subject, title, score, max_score, due_date , assignment_type):
        self.subject = subject.lower().strip()#strip() is used to remove any leading or trailing whitespace from the subject string and lower() is used to convert the subject string to lowercase.
        self.title = title
        self.score = float(score)
        self.max_score = float(max_score) 
        self.due_date = due_date
        self.type = assignment_type 
#This is an example of a class that represents an assignment with attributes such as subject, title, score, max_score, due_date, and type. 

home_work1=Assignment("Math", "Permutation Homework 1", 85, 100, "2023-09-15", "Homework")
#creating an object or instance of the Assignment class with the specified attributes.
print(home_work1.subject) 
 # Output: math
print(home_work1.title)  
 # Output: Homework 1
print(home_work1.score)   
# Output: 85.0
print(home_work1.max_score) 
 # Output: 100.0
print(home_work1.due_date) 
 # Output: 2023-09-15
print(home_work1.type)  
  # Output: Homework
class Home_work(Assignment):

# Inheriting the Assignment class to create a subclass for Homework assignments.
    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(subject, title, score, max_score, due_date, "Homework") 
#supper() is used to call the constructor of the parent class (Assignment) and pass the assignment_type as "Homework".

Homework2=Home_work("Chemistry", "Isotopes Homework 2", 90, 100, "2023-09-22") 
#this is an example of a class that represents a homework assignment with attributes such as subject, title, score, max_score, due_date, and type.
print(Homework2.subject) 
 # Output: chemistry
print(Homework2.title)  
 # Output: Isotopes Homework 2
print(Homework2.score) 
  # Output: 90.0
print(Homework2.max_score) 
 # Output: 100.0
print(Homework2.due_date)  
# Output: 2023-09-22
print(Homework2.type)   
 # Output: Homework

class Exam(Assignment):
 # Inheriting the Assignment class to create a subclass for Exam assignments.
    def __init__(self, subject, title, score, max_score, due_date):
# this is an example of a class that represents an exam assignment with attributes such as subject, title, score, max_score, due_date, and type.
        super().__init__(subject, title, score, max_score, due_date, "Exam")

 #supper() is used to call the constructor of the parent class (Assignment) and pass the assignment_type as "Exam". 
Exam1=Exam("Physics", "nuclear physics Exam 1", 95, 100, "2023-09-30")
print(Exam1.subject) 
 # Output: physics
print(Exam1.title)  
 # Output: nuclear physics Exam 1
print(Exam1.score)  
 # Output: 95.0
print(Exam1.max_score) 
 # Output: 100.0
print(Exam1.due_date)  
# Output: 2023-09-30
print(Exam1.type)   
 # Output: Exam

class GradeTracker:
    # This is an example of a class that represents a grade tracker with attributes such as assignments and methods to add assignments and calculate the average score.
    def __init__(self):
        self.assignments = [] 
    # This is an empty list that will hold all the assignments added to the grade tracker.
    def add_assignment(self, assignment):
        self.assignments.append(assignment)
    # This method takes an assignment object as input and appends it to the assignments list.
    def calculate_average(self):
        total_score = 0
    # this is a temporary variable/counter that will hold the total score of all assignments in the assignments list.
        total_max_score = 0
        for assignment in self.assignments:
            total_score += assignment.score 
    #and here is a loop that iterates(Go) through each assignment in the assignments list and adds its score to the total_score variable and its max_score to the total_max_score variable.
            total_max_score += assignment.max_score
    #+= means add the value on the right to the variable on the left and assign the result to the variable on the left.
        if total_max_score == 0:
            return 0 
    # and returns here means that if the total_max_score is 0, the method will return 0 to avoid division by zero error.
        return (total_score / total_max_score) * 100
    # This method calculates the average score of all assignments in the assignments list and returns it as a percentage.
    def list_assignments(self):
    #here is a method that lists all the assignments in the grade tracker with their subject, title, score, max_score, due_date, and type.
        for assignment in self.assignments:
            print(f"Subject: {assignment.subject}, Title: {assignment.title}, Score: {assignment.score}/{assignment.max_score}, Due Date: {assignment.due_date}, Type: {assignment.type}")
    #this method iterates through each assignment in the assignments list and prints its attributes in a formatted string.
    def filter_assignments(self,filter_type,filter_value):
        #Here is a method that filters the assignments in the grade tracker based on a specified filter type and filter value.
        result = []
        for assignment in self.assignments:
            #this method iterates through each assignment in the assignments list and checks if the assignment's attribute matches the specified filter type and filter value.
            if filter_type == "type" and assignment.type == filter_value:
                #This method checks if the filter type is "type" and if the assignment's type matches the filter value.
                result.append(assignment)
                #And if the condition is true, the assignment is added to the result list.
            elif filter_type == "subject" and assignment.subject == filter_value:
                # Here,If the filter type is "subject" and if the assignment's subject matches the filter value, it is added to the result list.
                result.append(assignment)
                #And if the condition is true, the assignment is added to the result list.
            elif filter_type == "month" and assignment.due_date.startswith(filter_value):#startswith() is a method that checks if the due_date string starts with the specified filter value (month).
                result.append(assignment)
        return result
    def highest_score_assignment(self):
        highest=self.assignments[0]
        for assignment in self.assignments:
            if assignment.score > highest.score:
                highest = assignment    
        return highest

    def lowest_score_assignment(self):
        lowest=self.assignments[0]
        for assignment in self.assignments:
            if assignment.score < lowest.score:
                lowest = assignment
        return lowest
    def per_subject_average(self):
        subject_scores = {}
        subject_max_scores = {}
        for assignment in self.assignments:
            if assignment.subject not in subject_scores:
                subject_scores[assignment.subject] = 0
                subject_max_scores[assignment.subject] = 0
            subject_scores[assignment.subject] += assignment.score
            subject_max_scores[assignment.subject] += assignment.max_score
        averages = {}
        for subject in subject_scores:
            if subject_max_scores[subject] > 0:
                averages[subject] = (subject_scores[subject] / subject_max_scores[subject]) * 100
            else:
                averages[subject] = 0
        return averages
#below code if for testing the filter_assignments method by filtering assignments based on type, subject, and month .
tracker=GradeTracker() 
#creating an object or instance of the GradeTracker class.
tracker.add_assignment(home_work1)
 #adding the home_work1 assignment to the grade tracker.  
tracker.add_assignment(Homework2)
 #adding the Homework2 assignment to the grade tracker.
tracker.add_assignment(Exam1)
 #adding the Exam1 assignment to the grade tracker.
average_score = tracker.calculate_average() 
#calculating the average score of all assignments in the grade tracker.
print(f"The overall average score is: {average_score:.2f}")
 # Output: The overall average score is: 90.00
print("\nAll assignments:")
tracker.list_assignments()#this method calls the list_assignments method to print all the assignments in the grade tracker. 
#calling the list_assignments method to print all the assignments in the grade tracker.
print("\nHomework assignments:")
Homework_assignments = tracker.filter_assignments("type", "Homework")
for assignment in Homework_assignments:
    print(f"Subject: {assignment.subject}, Title: {assignment.title}, Score: {assignment.score}/{assignment.max_score}, Due Date: {assignment.due_date}, Type: {assignment.type}")
    
highest_assignment =tracker.highest_score_assignment()
print(f"\nHighest score assignment: Subject: {highest_assignment.subject}, Title: {highest_assignment.title}, Score: {highest_assignment.score}/{highest_assignment.max_score}, Due Date: {highest_assignment.due_date}, Type: {highest_assignment.type}")
lowest_assignment = tracker.lowest_score_assignment() 
print(f"\nLowest score assignment: Subject: {lowest_assignment.subject}, Title: {lowest_assignment.title}, Score: {lowest_assignment.score}/{lowest_assignment.max_score}, Due Date: {lowest_assignment.due_date}, Type: {lowest_assignment.type}")  

def get_non_empty_input(message: str) -> str:
    while True:
        user_input = input(message).strip()
        if user_input!= "":
            return user_input
        print("Input cannot be empty. Please try again.")
def get_score(message, max_score) -> float:#here i am using a function to get a valid score input from the user. It takes a message to display to the user and the maximum score as parameters. The function will keep prompting the user until they enter a valid numeric score between 0 and the maximum score.
    while True:
        try:
            score = float(input(message))
            if 0 <= score <= max_score:
                return score
            else:
                print(f"Score must be between 0 and {max_score}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_due_date(message):
    while True:
        due_date = input(message).strip()
        if len(due_date) == 10 and due_date[4] == '-' and due_date[7] == '-' and due_date[:4].isdigit() and due_date[5:7].isdigit() and due_date[8:].isdigit():
            return due_date
        else:
            print("Invalid date format. Please enter the date as YYYY-MM-DD.")
def add_homework(tracker):#This function is for adding a homework assignment to the grade tracker. It prompts the user to enter the subject, title, maximum score, score, and due date for the homework, creates a Homework object with the provided information, and adds it to the grade tracker.
    subject =input("Enter the subject: ").strip()
    title = input("Enter the title: ").strip()
    max_score = float(input("Enter the maximum score: ").strip())   
    score=float(input(f"Enter the score (0 to {max_score}): ").strip())
    due_date = input("Enter the due date (YYYY-MM-DD): ").strip()
    homework=Home_work(subject, title, score, max_score, due_date)
    tracker.add_assignment(homework)
    print("Homework added successfully.")


def add_exam(tracker):#and this is for adding an exam assignment to the grade tracker. It prompts the user to enter the subject, title, maximum score, score, and due date for the exam, creates an Exam object with the provided information, and adds it to the grade tracker.
    subject = input("Enter the subject: ").strip()
    title = input("Enter the title: ").strip()
    max_score = float(input("Enter the maximum score: ").strip())   
    score = float(input(f"Enter the score (0 to {max_score}): ").strip())
    due_date = input("Enter the due date (YYYY-MM-DD): ").strip()
    exam = Exam(subject, title, score, max_score, due_date)
    tracker.add_assignment(exam)
    print("Exam added successfully.")


def display_assignments(assignments):#this one is just a function that takes a list of assignments as input and displays their subject, title, score, max_score, due_date, and type in a formatted string. If the list is empty, it prints a message indicating that no assignments were found.
    if len(assignments) == 0:
        print("No assignments found.")
        return
    for assignment in assignments:
        print(f"Subject: {assignment.subject}, Title: {assignment.title}, Score: {assignment.score}/{assignment.max_score}, Due Date: {assignment.due_date}, Type: {assignment.type}")

def filter_assignments_menu(tracker):#Here i am trying to filter the assignments based on the user's input for type, subject, or month. The function prompts the user to enter a filter type and value, then calls the filter_assignments method of the GradeTracker class to get the filtered assignments and displays them.
    filter_type = input("Filter by (type/subject/month): ").strip().lower()
    filter_value=input(f"Enter the {filter_type} to filter by: ").strip().lower()
    filtered_assignments = tracker.filter_assignments(filter_type, filter_value)
    display_assignments(filtered_assignments)

def display_menu():#This one represents the menu that is displayed to the user when they run the grade tracker program. It lists the available options for adding homework, adding exams, listing assignments, filtering assignments, showing a summary of assignments, and exiting the program.
    print("\nGrade Tracker Menu:")
    print("1. Add Homework")
    print("2. Add Exam")
    print("3. List All Assignments")
    print("4. Filter Assignments")
    print("5. Show Summary")
    print("6. Exit")
    print("Please choose an option (1-6):")
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ").strip()
    if choice == "1":
        print("You chose to add Homework.")
        add_homework(tracker)
    elif choice == "2": 
        print("You chose to add Exam.")
        add_exam(tracker)
    elif choice == "3":
        print("You chose to list all assignments.")
        tracker.list_assignments()
    elif choice == "4":
        print("You chose to filter assignments.")
        filter_assignments_menu(tracker) 
    elif choice == "5":
        print(f"Overall average score: {tracker.calculate_average():.2f}%")
        highest_assignment = tracker.highest_score_assignment()
        lowest_assignment = tracker.lowest_score_assignment()
        print(f"Highest assignment: {highest_assignment.title} with a score of {highest_assignment.score}/{highest_assignment.max_score}")
        print(f"Lowest assignment: {lowest_assignment.title} with a score of {lowest_assignment.score}/{lowest_assignment.max_score}")
    elif choice == "6":
        print("Exiting the Grade Tracker. Goodbye!")
        print("Thank you for using the Grade Tracker! We hope it helped you keep track of your assignments and scores. Goodbye!")
        break

