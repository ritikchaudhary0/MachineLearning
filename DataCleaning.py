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
