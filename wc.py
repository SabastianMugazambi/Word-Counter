# Word counting text files by Sabastian Mugazambi

#Obtaining full name of file from the User
user_input = raw_input('Enter the full name of the file to check: ')
file_handle = open(user_input) #I am assigning a file handle for this file so that I will be able to use it in the loop. 

# I am assigning initial values to my variables representing the words,characters and lines.
my_lines = 0
my_words = 0
my_chars = 0

#Loop counts the characters, splits the lines into different strings and counts the characters in the strings.
for line in file_handle:
    words = line.split()
    my_lines = my_lines + 1
    my_words = my_words + len(words)
    my_chars = my_chars + len(line)
    
# Printing my findings. 
print "Lines:",my_lines
print "Words:",my_words
print "Characters:",my_chars  

file_handle.close() #Making sure to close the file. 