# Author:    Ayeon Lee
# Partner:   None
# Date:      01-08-2026
# Course:    CS 1400, University of Utah, Kahlert School of Computing
# Copyright: CS 1400 and Ayeon - This work may not
#            be copied for use in Academic Coursework.
#
# I, Ayeon Lee, certify that I wrote this code from scratch and
# did not copy it in part or whole from another source.
#
# File Contents/Program Purpose
#
#   Calculates the user’s final course grade according to the CS 1400 syllabus,
#   using several hypothetical midterm averages (0, 20, 40, 60, 80, 100).

user = input("Please enter your name: ")
assignments = input("Please enter your assignments scores: ")
quizzes = input("Please enter your quizzes scores: ")
labs = input("Please enter your labs scores: ")

assign_weight = float(assignments)*0.1
quizzes_weight = float(quizzes)*0.25
labs_weight = float(labs)*0.1

weight_sum = assign_weight + quizzes_weight + labs_weight

midterm_value = [0, 20, 40, 60, 80, 100]
for midterm in midterm_value:
    final_numeric_sum = weight_sum + midterm*0.55
    final_percentage = final_numeric_sum/100
    final_grade = final_percentage*100

    print(f"{user}, if your midterm score is {midterm}, your final grade is {final_grade: .2f}%.")
