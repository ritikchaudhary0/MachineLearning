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
"""
Even though we have cleaned the data, we have to convert these values to numeric types so we can analyze them. 
Some of the rows have missing values, so we'll need to handle those as well.

We convert both the birth and death date to numeric types. And also conver the Date column into numeric. And using this we avoided the empty string.
"""
from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Convert data column in numeric value
for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date


### Calculating Artist Ages----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
 we're going to work on calculating the ages at which age artists created their works of art.

 Those age less than 20 or negativ, we'll take care of these by categorizing artists younger than 20 as "Unknown"
"""

ages = []
for row in moma:
    date = row[6]
    birth = row[3]
    
    #print(birth)
    
    if type(birth) == int:
        age = date - birth
        #print(age)
    elif type(birth) != int:
        age = 0
    ages.append(age)
    
final_ages = []""
for check_age in ages:
    if check_age > 20:
        final_age = check_age
    else:
        final_age = 'Unknown'
    final_ages.append(final_age)
    
#print(ages)


# Converting Ages to Decades-----------------------------------------------------------------------------------------------------------------------------------------------
"""
We now have a list — ages — containing the artist ages when they created their artwork. Everyone have unique ages.
so we can calculate the decade during which the artist created each work. For instance, if we calculate that the artist was 24, we'll record that as the artist being in their 20s.
24 will become 2.
**Python stores strings in a list-like structure, which lets us slice them in the same way we would a list**

Let's take our final_ages list, loop over it, and perform the operation above to convert it into a list of decades.
"""
# The final_ages variable is available
# From the above code
decades = []
for age in final_ages:
    if age == "Unknown":
        decade = age
    else:
        decade = str(age)
        decade = decade[:-1] + '0s'
    
    decades.append(decade)


# Summarizing the Decade Data--------------------------------------------------------------------------------------------------------------------------------------------------------
"""
On the above code, we did the following:
---Calculated the age of the artists when they created their artwork.
---Simplified those ages to a list of "decades" so there were fewer unique values.

Now we wiil calculate that how much time the decades value occur. We did this using Dictonary, we can use sorting but in python we have dictionary feature, so we will use dictonary(it have the key:value feature).
"""

decade_frequency = {}
for item in decades:
    if item not in decade_frequency:
        decade_frequency[item] = 1
    else:
        decade_frequency[item] += 1
        
print(decade_frequency)

#Output {'30s': 4722, '60s': 1357, '70s': 559, '40s': 4081, '50s': 2434, '20s': 1856, 'Unknown': 1093, '90s': 253, '80s': 364, '100s': 3, '110s': 3}

# Inserting Variables into Strings---------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Most of what i have did so far is about cleaning and interpreting data stored in string form.
Another common application of strings is displaying output in an easy-to-read form.

The {str.format()} method is a powerful tool that helps us write easy-to-read code while combining strings with other variables.
output = "{}'s favorite number is {}".format("Kylie", 8)
output = "{0}'s favorite number is {1}, {1} is {0}'s favorite number".format("Kylie", 8)
template = "{name}'s favorite number is {num}, {num} is {name}'s favorite number"
   output = template.format(name="Kylie", num="8")
"""


