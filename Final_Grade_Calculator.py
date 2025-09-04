# Author: Pranit Yadav
# Program Description: This program calculates the final numeric and letter gradeof someone
# based on three exams, homework, a research project, and final project (with set weights))


# Weight values for each grading component
examWeight = 0.2
homeworkWeight = 0.2
researchWeight = 0.1
finalWeight = 0.1

# Function to get a valid grade input from the user (0-100)
def getGrade(prompt):
    grade = float(input(prompt))
    while grade < 0 or grade > 100:  # Validate input range
        print("Grade must be a number between 0 and 100.")
        grade = float(input(prompt))
    return grade

# Function to calculate the final numeric grade based on weighted components
def calcAverage(exam1, exam2, exam3, homework, research, final):
    examOne = exam1 * examWeight
    examTwo = exam2 * examWeight
    examThree = exam3 * examWeight
    homeworkAssignments = homework * homeworkWeight
    researchProject = research * researchWeight
    finalProject = final * finalWeight

    # Total weighted average
    numericGrade = examOne + examTwo + examThree + homeworkAssignments + researchProject + finalProject
    return numericGrade

# Function to convert numeric grade to letter grade
def calcLetter(grade):
    if grade < 59.50:
        return "F"
    elif grade >= 59.50 and grade < 69.50:
        return "D"
    elif grade >= 69.50 and grade < 79.50:
        return "C"
    elif grade >= 79.50 and grade < 89.50:
        return "B"
    else:
        return "A"

# Main function to run the grading program
def main():
    # Collect all required grades from user input
    exam1 = getGrade("What is your grade for Exam 1? " )
    exam2 = getGrade("What is your grade for Exam 2? ")
    exam3 = getGrade("What is your grade for Exam 3? ")
    homework = getGrade("What is your grade for Homework? ")
    research = getGrade("What is your grade for Research Project? ")
    final = getGrade("What is your grade for Final Project? ")

    # Calculate numeric and letter grades
    numericGrade = calcAverage(exam1, exam2, exam3, homework, research, final)
    letterGrade = calcLetter(numericGrade)

    # Display results
    print("Final Numeric Grade:", format(numericGrade, ".2f"))
    print("Final Letter Grade:", letterGrade)

# Call the main function to execute the program
main()




