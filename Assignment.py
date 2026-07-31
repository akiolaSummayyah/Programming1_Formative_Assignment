class Assignment: 
    def __init__(self, subject, title, score, max_score, due_date , assignment_type):
        self.subject = subject.lower().strip()
        self.title = title
        self.score = float(score)
        self.max_score = float(max_score) 
        self.due_date = due_date
        self.type = assignment_type # This is the Blueprint for this assignment.
        #This is an example of a class that represents an assignment with attributes such as subject, title, score, max_score, due_date, and type. 
home_work1=Assignment("Math", "Permutation Homework 1", 85, 100, "2023-09-15", "Homework")
print(home_work1.subject)  # Output: math
print(home_work1.title)   # Output: Homework 1
print(home_work1.score)   # Output: 85.0
print(home_work1.max_score)  # Output: 100.0
print(home_work1.due_date)  # Output: 2023-09-15
print(home_work1.type)    # Output: Homework
        


