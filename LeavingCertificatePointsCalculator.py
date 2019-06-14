#Global Array:

higher_level = ["h", "a", "hl", "al", "higher", "higher level", "honours", "honours level", "honors" "honors level", "hons", "ardleibheal", "ard"]
ordinary_level = ["o", "p", "g", "ol", "gl", "ordinary", "ordinary level", "pass", "pass level", "gnath", "gnathleibheal",]
foundation_level = ["f", "b", "fl", "bl", "foundation", "foundation level", "bonn", "bonnleibheal"]

higher_grades = ["h8", "h7", "h6" ,"h5" ,"h4", "h3", "h2", "h1"]
higher_grade_points = [0, 37, 46, 56, 66, 77, 88, 100]

ordinary_grades = ["o8", "o7", "o6" ,"o5" ,"o4", "o3", "o2", "o1"]
ordinary_grade_points = [0, 0, 12, 20, 28, 37, 46, 56]

foundation_grades = ["f2", "f1"]
foundation_grade_points = [12, 20]

common_grades = ["ungraded", "fail", "pass", "merit", "distinction"]
common_grade_points = [0, 0, 28, 46, 66]

maths = ["maths", "math", "mathematic", "mathematics", "arithmetic", "matamaitic", "mata",]
irish = ["irish", "gaeilge"]
lcvp = ["lcvp", "leaving certificate vocational program", "leaving cert vocational programme", "leaving certificate vocational program", "leaving certificate vocational programme"]

point_list = []
shortlist = []
total_points = 0

import unicodedata
def remove_diacritic(input):
    return unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')

number_of_subjects = int(input("How many subjects did you sit for your Leaving Certificate? Please input as a number (e.g. \"1\" not \"one\"): "))
for i in range(number_of_subjects):


    subject = input("Name a subject you took for the Leaving Certificate. ")
    lowered_subject = str.lower(subject)

    if lowered_subject in lcvp:
        level = "common"
        sanitised_level = level

    else:
        if lowered_subject in irish or lowered_subject in maths:
            level = str.lower(input("Did you sit Higher, Ordinary or Foundation Level {}? ".format(subject)))
            sanitised_level = level

        else:
            level = str.lower(input("Did you sit Higher or Ordinary Level {}? ".format(subject)))
            sanitised_level = level


    if sanitised_level in higher_level:
        higher_grade = str.lower(input("What grade did you achieve in Higher Level {}? ".format(subject)))
        for grade in higher_grades:
            if grade == higher_grade:
                points = higher_grade_points[higher_grades.index(grade)]
                if str.lower(subject) in maths:
                    if points >= 46:
                        points = points + 25
                print("You receieved {} points from this subject.".format(str(points)))
                #Alternative: print("From this subject, your points were " + str(points))
                point_list.append(points)

    if sanitised_level in ordinary_level:
        ordinary_grade = str.lower(input("What grade did you achieve in Ordinary Level {}? ".format(subject)))
        for grade in ordinary_grades:
            if grade == ordinary_grade:
                points = ordinary_grade_points[ordinary_grades.index(grade)]
                print("You receieved {} points from this subject.".format(str(points)))
                #Alternative: print("From this subject, your points were " + str(points))
                point_list.append(points)

    if sanitised_level in foundation_level:
        foundation_grade = str.lower(input("What grade did you achieve in Foundation Level {}? ".format(subject)))
        for grade in foundation_grades:
            if grade == foundation_grade:
                points = foundation_grade_points[foundation_grades.index(grade)]
                print("You receieved {} points from this subject.".format(str(points)))
                #Alternative: print("From this subject, your points were " + str(points))
                point_list.append(points)

    if sanitised_level == "common":
        common_grade = str.lower(input("What grade did you achieve in {}? ".format(subject)))
        for grade in common_grades:
            if grade == common_grade:
                points = common_grade_points[common_grades.index(grade)]
                print("You receieved {} points from this subject.".format(str(points)))
                #Alternative: print("From this subject, your points were " + str(points))
                point_list.append(points)

point_list.sort(reverse = True)
shortlist = point_list[:6]
total_points = sum(shortlist)
print("Total Points:", total_points)
