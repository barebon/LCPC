# Imported Modules:

from unidecode import unidecode as remove_diacritic

# Global Array:

word_numbers = ["zero", "0", "one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9", "ten", "10", "eleven", "11", "twelve", "12"]
numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]

higher_level = ["h", "a", "hl", "al", "higher", "higher level", "honours", "honours level", "honors" "honors level", "hons", "ardleibheal", "ard"]
ordinary_level = ["o", "p", "g", "ol", "gl", "ordinary", "ordinary level", "pass", "pass level", "gnath", "gnathleibheal",]
foundation_level = ["f", "b", "fl", "bl", "foundation", "foundation level", "bonn", "bonnleibheal"]

higher_grades = ["h8", "h7", "h6" ,"h5" ,"h4", "h3", "h2", "h1"]
higher_grade_points = [0, 37, 46, 56, 66, 77, 88, 100]

ordinary_grades = ["o8", "o7", "o6" ,"o5" ,"o4", "o3", "o2", "o1"]
ordinary_grade_points = [0, 0, 12, 20, 28, 37, 46, 56]

foundation_grades = ["f8", "f7", "f6", "f5", "f4", "f3", "f2", "f1"]
foundation_grade_points = [0, 0, 0, 0, 0, 0, 12, 20]

common_grades = ["ungraded", "fail", "pass", "merit", "distinction"]
common_grade_points = [0, 0, 28, 46, 66]

maths = ["maths", "math", "mathematic", "mathematics", "arithmetic", "matamaitic", "mata",]
irish = ["irish", "gaeilge"]
lcvp = ["lcvp", "leaving certificate vocational program", "leaving cert vocational programme", "leaving certificate vocational program", "leaving certificate vocational programme"]

point_list = []
shortlist = []
total_points = 0

# Body:
# Copyright notice, header text & initial question:

print("""Leaving Certificate Points Calculator [Version 1.0]
Copyright (c) 2019 Cian Finnegan under GNU Affero General Public License v3.0.
All rights reserved.

Note: This program can only accept grades from the new Common Points Scale (2017 onwards).
If you sat your exams in 2016 or before, please convert your grades to those of equivalent
points on the new scale (a converter is available at https://www.cao.ie/index.php?page=newcps/).

I hope this helps!

""")

word_number_of_subjects = str.lower(input("How many subjects did you sit for your Leaving Certificate?\n\n"))
number_of_subjects = numbers[word_numbers.index(word_number_of_subjects)]

# Loop:

for i in range(number_of_subjects):


    subject = input("Name a subject you took for the Leaving Certificate. ")
    lowered_subject = str.lower(subject)

    if lowered_subject in lcvp:
        level = "common"
        sanitised_level = "common"

    else:
        if lowered_subject in irish or lowered_subject in maths:
            level = str.lower(input("Did you sit Higher, Ordinary or Foundation Level {}? ".format(subject)))
            sanitised_level = remove_diacritic(level)

        else:
            level = str.lower(input("Did you sit Higher or Ordinary Level {}? ".format(subject)))
            sanitised_level = remove_diacritic(level)


    if sanitised_level in higher_level:
        higher_grade = str.lower(input("What grade (e.g. H2) did you achieve in Higher Level {}? ".format(subject)))
        for grade in higher_grades:
            if grade == higher_grade:
                points = higher_grade_points[higher_grades.index(grade)]
                if lowered_subject in maths:
                    if points >= 46:
                        points = points + 25
                print("You receieved {} points from this subject.".format(str(points)))
                point_list.append(points)

    if sanitised_level in ordinary_level:
        ordinary_grade = str.lower(input("What grade (e.g O2) did you achieve in Ordinary Level {}? ".format(subject)))
        for grade in ordinary_grades:
            if grade == ordinary_grade:
                points = ordinary_grade_points[ordinary_grades.index(grade)]
                print("You receieved {} points from this subject.".format(str(points)))
                point_list.append(points)

    if sanitised_level in foundation_level:
        foundation_grade = str.lower(input("What grade (e.g. F2) did you achieve in Foundation Level {}? ".format(subject)))
        for grade in foundation_grades:
            if grade == foundation_grade:
                points = foundation_grade_points[foundation_grades.index(grade)]
                print("You receieved {} points from this subject.".format(str(points)))
                point_list.append(points)

    if sanitised_level == "common":
        common_grade = str.lower(input("What grade (e.g Merit) did you achieve in {}? ".format(subject)))
        for grade in common_grades:
            if grade == common_grade:
                points = common_grade_points[common_grades.index(grade)]
                print("You receieved {} points from this subject.".format(str(points)))
                point_list.append(points)


# Calculation & Presentation:

point_list.sort(reverse = True)
shortlist = point_list[:6]
total_points = sum(shortlist)
print("Total Points:", total_points)
