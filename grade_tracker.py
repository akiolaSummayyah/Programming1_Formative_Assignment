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
