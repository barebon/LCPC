# Leaving Certificate Points Calculator [Version 1.1]
# Copyright (c) 2019 Cian Finnegan under GNU Affero General Public License v3.0.
# All rights reserved.


# Global Array:

word_numbers = ["zero", "0", "one", "1", "two", "2", "three", "3", "four", "4", "five", "5", "six", "6", "seven", "7", "eight", "8", "nine", "9", "ten", "10", "eleven", "11", "twelve", "12"]
numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]

higher_level = ["h", "a", "hl", "al", "higher", "higher level", "honours", "honours level", "honors" "honors level", "hons", "ardleibheal", "ardleibhéil" "ard"]
ordinary_level = ["o", "p", "g", "ol", "gl", "ordinary", "ordinary level", "pass", "pass level", "gnath", "gnáth", "gnathleibheal", "gnáthleibhéil"]
foundation_level = ["f", "b", "fl", "bl", "foundation", "foundation level", "bonn", "bonnleibheal", "bonnleibhéil"]

higher_grades = ["h8", "8", "h7", "7", "h6", "6", "h5", "5", "h4", "4", "h3", "3", "h2", "2", "h1", "1"]
higher_grade_points = [0, 0, 37, 37, 46, 46, 56, 56, 66, 66, 77, 77, 88, 88, 100, 100]

ordinary_grades = ["o8", "8", "o7", "7", "o6", "6", "o5", "5", "o4", "4", "o3", "3", "o2", "2", "o1", "1"]
ordinary_grade_points = [0, 0, 0, 0, 12, 12, 20, 20, 28, 28, 37, 37, 46, 46, 56, 56]

foundation_grades = ["f8", "8", "f7", "7", "f6", "6", "f5", "5", "f4", "4", "f3", "3", "f2", "2", "f1", "1"]
foundation_grade_points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 20, 20]

common_grades = ["ungraded", "fail", "níor éirigh leo", "nior eirigh leo", "níor éirigh", "nior eirigh", "pass", "pas", "merit", "tuillteanas", "distinction", "pas le gradam", "gradam"]
common_grade_points = [0, 0, 0, 0, 0, 0, 28, 28, 46, 46, 66, 66, 66]

maths = ["maths", "math", "mathematic", "mathematics", "arithmetic", "matamaitic", "mata",]
irish = ["irish", "gaeilge"]
lcvp = ["lcvp", "leaving certificate vocational program", "leaving cert vocational programme", "leaving certificate vocational program", "leaving certificate vocational programme", "gcat",
"gairmchlár na hardteistiméireachta", "gairmchlar na hardteistimeireachta", "gairmchlár", "gairmchlar"]

point_list = []
shortlist = []
total_points = 0

# Body:
# Copyright notice, header text & initial question:

print("""Leaving Certificate Points Calculator [Version 1.1]
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


    subject = input("\nName a subject you took for the Leaving Certificate.\n\n")
    lowered_subject = str.lower(subject)

    if lowered_subject in lcvp:
        level = "common"

    elif lowered_subject in irish or lowered_subject in maths:
        level = str.lower(input("\nDid you sit Higher, Ordinary or Foundation Level {}?\n\n".format(subject)))

    else:
        level = str.lower(input("\nDid you sit Higher or Ordinary Level {}?\n\n".format(subject)))


    if level in higher_level:
        higher_grade = str.lower(input("\nWhat grade (e.g. H2) did you achieve in Higher Level {}?\n\n".format(subject)))
        for grade in higher_grades:
            if grade == higher_grade:
                points = higher_grade_points[higher_grades.index(grade)]
                if lowered_subject in maths:
                    if points >= 46:
                        points = points + 25
                print("\nYou receieved {} points from this subject.\n".format(str(points)))
                point_list.append(points)

    if level in ordinary_level:
        ordinary_grade = str.lower(input("\nWhat grade (e.g O2) did you achieve in Ordinary Level {}?\n\n".format(subject)))
        for grade in ordinary_grades:
            if grade == ordinary_grade:
                points = ordinary_grade_points[ordinary_grades.index(grade)]
                print("\nYou receieved {} points from this subject.\n".format(str(points)))
                point_list.append(points)

    if level in foundation_level:
        foundation_grade = str.lower(input("\nWhat grade (e.g. F2) did you achieve in Foundation Level {}?\n\n".format(subject)))
        for grade in foundation_grades:
            if grade == foundation_grade:
                points = foundation_grade_points[foundation_grades.index(grade)]
                print("\nYou receieved {} points from this subject.\n".format(str(points)))
                point_list.append(points)

    if level == "common":
        common_grade = str.lower(input("\nWhat grade (e.g Merit) did you achieve in {}?\n\n".format(subject)))
        for grade in common_grades:
            if grade == common_grade:
                points = common_grade_points[common_grades.index(grade)]
                print("\nYou receieved {} points from this subject.\n".format(str(points)))
                point_list.append(points)


# Calculation & Presentation:

point_list.sort(reverse = True)
shortlist = point_list[:6]
total_points = sum(shortlist)
print("\nTotal Points:", total_points)
