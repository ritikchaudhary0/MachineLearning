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

# Replacing Substrings with the Replace Method.................................................................................................................................
#when we're cleaning data, we need to replace parts of strings so our data is consistent.   str.replace()
age1 = "I am thirty-one years old"
age2 = age1.replace('thirty-one','thirty-two')

# Cleaning the Nationality and Gender Columns....................................................................................................................................
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

# String Capitalization............................................................................................................................................................
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

# Errors During Data Cleaning...........................................................................................................................
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

# Parsing Numbers from Complex Strings, Part One.................................................................................................
# This column contains data in many different formats:
"""Some years are in parentheses.
Some years have c. or C. before them, indicating that the year is approximate.
Some have year ranges, indicated with a dash.
Some have 's to indicate a decade.
"""

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]
def strip_characters(string):
    for bad_char in bad_chars:
        string = string.replace(bad_char,"")
    return string

stripped_test_data = []
for str in test_data:
    cleaned_str = strip_characters(str)
    stripped_test_data.append(cleaned_str)



# Parsing Numbers from Complex Strings, Part Two.............................................................................................................................................
#now we've removed the "bad" characters from the numbers(years). 
"""
There are two different scenarios that we need to prepare for when converting these to integers:

Some are a single year (e.g., 1912).
Some are ranges of years (e.g., 1913-1923).

Here are the ways we'll treat the various cases:

Where there is a single year, we'll keep it.
Where there is a year range, we'll average the two years. For avg of two years we need to conver the number in int and then we can take the avg.
"""
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

def process_date(check_range):
    sum = 0
    if "-" in check_range:                  # remove that range(dash-) from the string number and converted that string into int.
        split_list = check_range.split("-")
        for string_value in split_list:
            conv_int = int(string_value)
            sum += conv_int
        avg = round(sum/2)
        return avg
    else:
        int_value = int(check_range)
        return int_value
    
processed_test_data = []
for check_range in stripped_test_data:
    clean_int_data = process_date(check_range)
    processed_test_data.append(clean_int_data)
    
for row in moma:
    date = row[6]
    remove_bad_char = strip_characters(date)
    convert_dates_into_int = process_date(remove_bad_char)
    row[6] = convert_dates_into_int


### Now we have to analysis the dataset.............................................................................................................................
