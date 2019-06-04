#Global Array:
med_points = 550 #Current points for med
Ordinary = ["ordinary", "ol", "ordinary level", "pass", "pass level"]
High_Grade_Names = ["h8", "h7", "h6" ,"h5" ,"h4", "h3", "h2", "h1"]
High_Grade_Points = [0, 37, 46, 56, 66, 77, 88, 100]
Ord_Grade_Names = ["o8", "o7", "o6" ,"o5" ,"o4", "o3", "o2", "o1"]
Ord_Grade_Points = [0, 0, 12, 20, 28, 37, 46, 56]
Maths_Names = ["maths", "math", "mathematic", "mathematics", "arithmetic"]
point_list = []
shortlist = []
total_points = 0

Number_Subjects = int(input("How many subjects did you sit for your Leaving Certificate? Please input as a number (e.g. \"1\" not \"one\"): "))
for i in range(Number_Subjects):
    Subject = input("Name a subject you took for the Leaving Certificate. ")

    level = str.lower(input("Did you sit Higher or Ordinary Level {}? ".format(Subject)))
    if level in Ordinary:
        Ord_Grade = str.lower(input("What grade did you achieve in Ordinary Level {}? ".format(Subject)))
        for grade in Ord_Grade_Names:
            if grade == Ord_Grade:
                points = Ord_Grade_Points[Ord_Grade_Names.index(grade)]
                print("You receieved {} points from this subject.".format(str(points)))
                #An alternative method to this is print("From this subject, your points were " + str(points))
                point_list.append(points)

    else:
        High_Grade = str.lower(input("What grade did you achieve in Higher Level {}? ".format(Subject)))
        for grade in High_Grade_Names:
            if grade == High_Grade:
                points = High_Grade_Points[High_Grade_Names.index(grade)]
                if str.lower(Subject) in Maths_Names:
                    if points >= 46:
                        points = points + 25
                print("You receieved {} points from this subject.".format(str(points)))
                #An alternative method to this is print("From this subject, your points were " + str(points))
                point_list.append(points)

point_list.sort(reverse = True)
shortlist = point_list[:6]
print(point_list)
print(shortlist)
print("Total Points: " + sum(shortlist))
