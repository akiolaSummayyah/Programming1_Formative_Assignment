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
