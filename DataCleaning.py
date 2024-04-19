#We use the len() function to count how many items (rows) are in the moma list of lists.
num_rows = len(moma)

"""
So we these columns in our MOMA dataset--------

Title: the title of the artwork
Artist: the name of the artist who created the artwork
Nationality: the nationality of the artist
BeginDate: the year in which the artist was born
EndDate: the year in which the artist died
Gender: the gender of the artist
Date: the date that the artwork was created
Department: the department inside MoMA to which the artwork belongs

"""
# Python has a built-in csv module that can handle the work of opening a CSV for us
from csv import reader

# Use the open() function to open the artworks.csv
opened_file = open('artworks.csv')

# Use the reader() function to parse the data from opened_file
read_file = reader(opened_file)

# Use list() to convert read_file into a list of lists
moma = list(read_file)

# Use list slicing to remove the column names (the first row) from the moma, becoz in data processing we don't need the header row that's why we removed it in cleaning.
moma = moma[1:]

# Replacing Substrings with the Replace Method.
#when we're cleaning data, we need to replace parts of strings so our data is consistent.   str.replace()
age1 = "I am thirty-one years old"
age2 = age1.replace('thirty-one','thirty-two')

# Cleaning the Nationality and Gender Columns.
# Remove the extra paranthesis from the data using str,replace() method.
for row in moma:
    nationality = row[2]
    nationality = nationality.replace('(','')
    nationality = nationality.replace(')','')
    row[2] = nationality 
    
    gender = row[5]
    gender = gender.replace('(','')
    gender = gender.replace(')','')
    row[5] = gender

# String Capitalization
#The str.title() method returns a copy of the string with the first letter of each word transformed to uppercase.
##We will not use str.replace() method for this because in replace we have to know what is needed to change {We could use str.replace() to replace m with M, but then we'd end up with instances of FeMale}

for row in moma:
    Gender = row[5]
    Gender = Gender.title()
    if not Gender:
        Gender = "Gender Unknown/Other"
    row[5] = Gender
    
    Nationality = row[2]
    Nationality = Nationality.title()
    if not Nationality:
        Nationality = "Nationality Unknown"
    row[2] = Nationality

# Errors During Data Cleaning
#Remove the string value from dates {'1996' strings value}. and convert it into int. We made a function for do this.

def clean_and_convert(date):
    # check that we don't have an empty string
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    BeginDate = row[3]
    EndDate = row[4]
    clean_begindate = clean_and_convert(BeginDate)
    clean_enddate = clean_and_convert(EndDate)
    row[3] = clean_begindate
    row[4] = clean_enddate

#
