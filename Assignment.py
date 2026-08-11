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
                # Here,If the filter type is "subject" and if the assignment's subject matches the filter value.
                    result.append(assignment)
                #And if the condition is true, the assignment is added to the result list.
                elif filter_type == "month" and assignment.due_date.startswith(filter_value):
                    result.append(assignment)
            return result
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