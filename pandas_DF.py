import pandas as pd

#So far, we've only dealt with 1D arrays, which are series.
#   Now we're going to talk about 2D arrays, which are data frames.
grades_dict = { "Wally":[87,96,70],
                "Eva":[100,87,90],
                "Sam":[94,77,90],
                "Katie":[100,81,82],
                "Bob":[83,65,85]}

#Convert to a data frame
grades = pd.DataFrame(grades_dict)
    #Each of the keys become columns, and each of the values
    #   in each key become the rows.

#Change the row indexes to custom indexes.
grades.index = ["Test1","Test2","Test3"]

print(grades)

eva = grades["Eva"]

sam = grades.Sam

#Using the loc and iloc methods

#Dataframes do support the brackets, but they strongly suggest
#   we use their custom methods to extract data
#   because they're more optimized for performance

test2 = grades.loc["Test2"]

test1 = grades.iloc[0]

#For consecutive rows - loc method
test1_thru_test3 = grades.loc["Test1":"Test3"]

#For nonconsecutive rows
test1_and_test3 = grades.loc[["Test1","Test3"]]
    #NOTE THE DOUBLE BRACKETS -- you need a list for nonconsecutive

#iloc method -- doesn't include upper bound
test1_and_test2 = grades.iloc[0:2]

#View only Eva's and Katie's grades for both Test1 and Test2
eva_katie_test1_test2 = grades.loc["Test1":"Test2",["Eva","Katie"]]
#eva_katie_test1_test2 = grades.loc[:"Test2",["Eva","Katie"]]
                                #Can also omit before : because it assumes the first


#View only Sam's THROUGH Bob's grades for Test1 and Test3
sam_thru_bob_test1_test3 = grades.loc[["Test1","Test3"],"Sam":"Bob"]
#sam_thru_bob_test1_test3 = grades.loc[["Test1","Test3"],"Sam":]
                                #Can also omit before : because it assumes the last



#Boolean Indexing
#Select everyone with an A grade (90 or higher)
grades_A = grades[grades >= 90]

#Create a dataframe for everyone with a B grade
grades_B = grades[(grades >= 80) & (grades < 90)]

#Create a dataframe for everyone with an A or a B
grades_A_or_B = grades[(grades >= 90) | (grades >= 80)]


#Set overall precision at the pd level
pd.set_option("precision",2)

#By student
print(grades.describe())

#By test
print(grades.T.describe())
    #This transposes it

#Average of student grades on each test
print(grades.T.mean())


#Sort rows by their indexes (test name)
r_sorted_grades_i = grades.sort_index(ascending=False)

#Sort columns by their column names (student names)
# axis = 1 indicates to sort by column indexes
# axis = 2 indicates to sort by row indexes

c_sorted_grades_i = grades.sort_index(axis = 1)

#In reverse sort order
#c_sorted_grades_i = grades.sort_index(axis = 1, ascending = False)


print()