# Global Array:

# Directing many possible answers (including contractions, colloquialisms & the Irish language) for each level to one variable for each:
higher_level = ["h", "a", "hl", "al", "higher", "higher level", "honours", "honours level", "honors" "honors level", "hons", "ardleibheal", "ard"]
ordinary_level = ["o", "p", "g", "ol", "gl", "ordinary", "ordinary level", "pass", "pass level", "gnath", "gnathleibheal",]
foundation_level = ["f", "b", "fl", "bl", "foundation", "foundation level", "bonn", "bonnleibheal"]

# Creating parallel arrays to assign points values to grades at each level:
higher_grades = ["h8", "h7", "h6" ,"h5" ,"h4", "h3", "h2", "h1"]
higher_grade_points = [0, 37, 46, 56, 66, 77, 88, 100]

ordinary_grades = ["o8", "o7", "o6" ,"o5" ,"o4", "o3", "o2", "o1"]
ordinary_grade_points = [0, 0, 12, 20, 28, 37, 46, 56]

foundation_grades = ["f2", "f1"]
foundation_grade_points = [12, 20]

common_grades = ["ungraded", "fail", "pass", "merit", "distinction"]
common_grade_points = [0, 0, 28, 46, 66]

# Directing many possible answers (including contractions, colloquialisms & the Irish language) for some specific subjects to one variable for each:
# Certain subjects incur exceptions in the calculations process, and the program must recognise these.
maths = ["maths", "math", "mathematic", "mathematics", "arithmetic", "matamaitic", "mata",]
irish = ["irish", "gaeilge"]
lcvp = ["lcvp", "leaving certificate vocational program", "leaving cert vocational programme", "leaving certificate vocational program", "leaving certificate vocational programme"]

# Defining new empty arrays and variables:
point_list = []
shortlist = []
total_points = 0

# Importing the unidecode function from the unidecode module and renaming it to "remove_diacritic":
# This function removes accents from (sanitises) input strings, which functions in this case to strip the fada (acute) accent from any answers input in the Irish language.
from unidecode import unidecode as remove_diacritic

# Asking user how many subjects they sat:
number_of_subjects = int(input("How many subjects did you sit for your Leaving Certificate? Please input as a number (e.g. \"1\" not \"one\"): "))
# Creating a loop to repeat the points calculation process for each subject:
for i in range(number_of_subjects):

    # Asking the user for a subject they sat:
    subject = input("Name a subject you took for the Leaving Certificate. ")
    lowered_subject = str.lower(subject)

    # Checking if the input subject is LCVP and assigning the level as "common" if so, as is necessary:
    # LCVP is the only available Leaving Certificate subject which can only be sat at one level (Common level),
    # so the program can skip asking the user for the level at which they sat it.
    if lowered_subject in lcvp:
        level = "common"
        # The level can be considered sanitised as the word "common" contains no accents anyway.
        sanitised_level = "common"

    # All other subjects have at least two levels, and so require that the program ask and
    # account for the level which they sat, as part of the calculation process.
    else:
        # Checking if the input subject is either Maths or Irish and asking an alternate question, as is necessary:
        # Irish and Maths are the only two Leaving Certificate subjects with an extra level below Ordinary level (Foundation level),
        # so the question asking the user for the level at which the user sat these subjects must be adjusted to include this.
        if lowered_subject in irish or lowered_subject in maths:
            level = str.lower(input("Did you sit Higher, Ordinary or Foundation Level {}? ".format(subject)))
            # Removing accents from the user's answer:
            sanitised_level = remove_diacritic(level)

        # All other subjects require the standard question asking the user for the level at which they sat the subject:
        else:
            level = str.lower(input("Did you sit Higher or Ordinary Level {}? ".format(subject)))
            # Removing accents from the user's answer:
            sanitised_level = remove_diacritic(level)

    # Here are four different routes the answered subject can take. Which one is taken depends on the level at which the subject was sat:

    # Checking if the user's answer is one of the names or contractions for Higher level listed at the top in the global array:
    # If it was sat at Higher level, the subject follows this route.
    if sanitised_level in higher_level:
        # Asking the user for the grade they achieved in the subject:
        # The answer is automatically adjusted to be all lowercase, removing the need to duplicate each grade in both lowercase
        # and uppercase in the array at the top (e.g. "H1" automatically becomes "h1").
        # The last word of the question is the subject that the user input, so it just copies their answer into the curly brackets.
        higher_grade = str.lower(input("What grade did you achieve in Higher Level {}? ".format(subject)))
        # Checking the user's achieved grade against the list of Higher level grades until it finds a match:
        for grade in higher_grades:
            if grade == higher_grade:
                # Finding the point value of the matched grade from the parallel list and saves it as the variable "points":
                points = higher_grade_points[higher_grades.index(grade)]
                # Checking if the input subject is Maths, then checking if the student achieved a H6 grade or higher
                # (a H6 awards the student 46 points), and assigning an extra 25 points if both are true:
                # Students who achieve a H6 grade or above in Higher level Maths are awarded an extra 25 points as an incentive to
                # take the disproportionately difficult subject at Higher level.
                if str.lower(subject) in maths:
                    if points >= 46:
                        points = points + 25
                # Telling the user how many points they were awarded for this subject:
                # An alternative method to this is print("From this subject, your points were " + str(points))
                print("You receieved {} points from this subject.".format(str(points)))
                # Adding the points awarded for this subject to the list of earned points:
                point_list.append(points)

    # Checking if the user's answer is one of the names or contractions for Ordinary level listed at the top in the global array:
    # If it was sat at Ordinary level, the subject follows this route.
    if sanitised_level in ordinary_level:
        # Asking the user for the grade they achieved in the subject:
        # The answer is automatically adjusted to be all lowercase, removing the need to duplicate each grade in both lowercase
        # and uppercase in the array at the top (e.g. "O1" automatically becomes "o1").
        # The last word of the question is the subject that the user input, so it just copies their answer into the curly brackets.
        ordinary_grade = str.lower(input("What grade did you achieve in Ordinary Level {}? ".format(subject)))
        # Checking the user's achieved grade against the list of Ordinary level grades until it finds a match:
        for grade in ordinary_grades:
            if grade == ordinary_grade:
                # Finding the point value of the matched grade from the parallel list and saves it as the variable "points":
                points = ordinary_grade_points[ordinary_grades.index(grade)]
                # Telling the user how many points they were awarded for this subject:
                # An alternative method to this is print("From this subject, your points were " + str(points))
                print("You receieved {} points from this subject.".format(str(points)))
                # Adding the points awarded for this subject to the list of earned points:
                point_list.append(points)

    # Checking if the user's answer is one of the names or contractions for Foundation level listed at the top in the global array:
    # If it was sat at Foundation level, the subject follows this route.
    if sanitised_level in foundation_level:
        # Asking the user for the grade they achieved in the subject:
        # The answer is automatically adjusted to be all lowercase, removing the need to duplicate each grade in both lowercase
        # and uppercase in the array at the top (e.g. "F1" automatically becomes "f1").
        # The last word of the question is the subject that the user input, so it just copies their answer into the curly brackets.
        foundation_grade = str.lower(input("What grade did you achieve in Foundation Level {}? ".format(subject)))
        # Checking the user's achieved grade against the list of Foundation level grades until it finds a match:
        for grade in foundation_grades:
            if grade == foundation_grade:
                # Finding the point value of the matched grade from the parallel list and saves it as the variable "points":
                points = foundation_grade_points[foundation_grades.index(grade)]
                # Telling the user how many points they were awarded for this subject:
                # An alternative method to this is print("From this subject, your points were " + str(points))
                print("You receieved {} points from this subject.".format(str(points)))
                # Adding the points awarded for this subject to the list of earned points:
                point_list.append(points)

    # Checking if the level was automatically set to "common" earlier:
    # If the subject is LCVP, it follows this route (as LCVP is the only subject with a Common level):
    if sanitised_level == "common":
        # Asking the user for the grade they achieved in the subject:
        # The answer is automatically adjusted to be all lowercase, removing the need to duplicate each grade in both lowercase
        # and uppercase in the array at the top (e.g. "Merit" automatically becomes "merit").
        # The last word of the question is the subject that the user input, so it just copies their answer into the curly brackets.
        # I could have instead just made the last word "LCVP" as it is currently the only subject with a Common level, but this method
        # allows for easier future addition of any new subjects with a Common level.
        common_grade = str.lower(input("What grade did you achieve in {}? ".format(subject)))
        # Checking the user's achieved grade against the list of Common level grades until it finds a match:
        for grade in common_grades:
            if grade == common_grade:
                # Finding the point value of the matched grade from the parallel list and saves it as the variable "points":
                points = common_grade_points[common_grades.index(grade)]
                # Telling the user how many points they were awarded for this subject:
                # An alternative method to this is print("From this subject, your points were " + str(points))
                print("You receieved {} points from this subject.".format(str(points)))
                # Adding the points awarded for this subject to the list of earned points:
                point_list.append(points)

# Sorting the list of earned points from highest to lowest:
point_list.sort(reverse = True)
# Creating a shortlist of the first (highest) six subjects' points on the list:
shortlist = point_list[:6]
# Adding together the six subjects' points from the shortlist.
total_points = sum(shortlist)
# Telling the user the final count of points:
print("Total Points:", total_points)
