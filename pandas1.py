import pandas as pd     #pd is the common alias for pandas

grades = pd.Series([87,100,94])

#print(grades)

a = pd.Series(98.6, range(3))

#print()

b = grades[0]
c = grades.count()
d = grades.mean()

#print(grades.describe())

#Add custom indexing.
grades = pd.Series([87,100,94], index = ["Wally","Eva","Sam"])

#print(grades)

grades_dict = {"Wally":87, "Eva":100,"Sam":94}
    #In this case, the keys become the indexes, and the values
    #   become the columns in the data series. In this case, you
    #   don't have to specify the indexes.


grades_ds = pd.Series(grades_dict)


print(grades_ds)


#These next two statements do the same thing.
eva = grades["Eva"]
wally = grades.Wally    #The dot method only works on string indexes.

print(eva, wally)
