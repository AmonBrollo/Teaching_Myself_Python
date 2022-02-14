"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    # Create a list for use
    students = []
    # Get the number of students and iterate through those students
    for _ in range(int(input())):
        # Get the name
        name = input()
        #Get the grade
        score = float(input())
        # Make the created list a nested list with each name and grade
        students.append([name, score])
    # list is now:
    # [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], 
    # ['Harsh', 39.0]]

    # Sort the list by grade. Lambda allows for a 1 time function to sort 
    # the nested list by grade 
    students = sorted(students, key = lambda x: x[1])
    # List is now:
    # [['Tina', 37.2], ['Harry', 37.21], ['Berry', 37.21], ['Harsh', 39.0], 
    # ['Akriti', 41.0]]

    # Get the second lowest score.
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
    # Create a list for students with the second lowest scores.
    desired_students = []
    # Iterate throught students.
    for stu in students:    
        # Find the name os the students with the second lowest scores.
        if stu[1] == second_lowest_score:
            # Put them on the list
            desired_students.append(stu[0])
    # Display the students with the second lowest scores
    print("\n".join(sorted(desired_students)))

"""
Questions that need answers:
What exactly is happening in line 33 with the "set" attribure? 
And why do we need the "[1]" there?
"""