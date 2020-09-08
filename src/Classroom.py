#Three dictionaries for three different students
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

#Function takes list of numbers and returns the average
def average(numbers):
    total = sum(numbers)
    length = len(numbers)
    return float(total)/length

#Function takes a student dictionary as input and returns their weighted average
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

#Function takes score number and returns letter grade
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#Function calculates class average by getting average for each student then the average of those
def get_class_average(class_list):
    results =[]
    for student in class_list:
        results.append(get_average(student))
    return average(results)

#Lloyd average
print ("Lloyd's average grade is: " + get_letter_grade(get_average(lloyd)))

#Average of class
students = [alice, lloyd, tyler]
print ("The number average of the class is: %.2f " % get_class_average(students))

#Letter grade of class average
print ("The class average letter grade is: " + get_letter_grade(get_class_average(students)))
