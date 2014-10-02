# Regular expressions activity II
# Learning about Python regex Match objects.

import re

def main():
    poem = readShel()
    printFirstRegexMatch(r'[\s\w][Oo]ut', poem)

def readShel():
    '''Reads the Shel Silverstein poem and returns a string.'''
    filename = 'poem.txt'
    f = open(filename,'r')
    poem = f.read()
    f.close()
    return poem

def printFirstRegexMatch(pattern, text):
    '''Prints the first occurrence of the regular expression.'''
    m = re.search(pattern, text)

    # New type!  m is a "match object".
    print "re.search() returned an object of type: " + str(type(m))

    # What methods do match objects have?  Well...
    first_matched_string = m.group(0)
    print 'The first match of "%s" in your text is "%s",' % (pattern, first_matched_string)
    start_index = m.start(0)
    end_index = m.end(0)
    print 'which starts at index %d and ends at %d.' % (start_index, end_index)

main()
