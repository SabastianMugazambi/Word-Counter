# Regular expressions activity III
# Learning about regex match iterators.

import re

def main():
    poem = readShel()
    printRegexMatches(r'.\'.', poem)

def readShel():
    '''Reads the Shel Silverstein poem and returns a string.'''
    filename = 'poem.txt'
    f = open(filename,'r')
    poem = f.read()
    f.close()
    return poem

def printRegexMatches(pattern, text):
    '''Prints all occurrences of the regular expression.'''
    match_iter = re.finditer(pattern, text)

    # New type!  match_iter is a sort of "iterator".
    print "re.finditer() returned an object of type: " + str(type(match_iter))

    # An iterator is something that a for-loop can loop over.
    #   A match iterator, specifically, is one that makes the loop variable be
    # a match object each time.  So now, rather than just finding the first
    # match, we can iterate over *all* matches.

    print 'Your pattern, "%s", matches the text:' % pattern
    for occurrence in match_iter:
        print '  %s at indices %d--%d' % (
            occurrence.group(0), occurrence.start(0), occurrence.end(0))
        # Note: inside parentheses, I can continue a single statement on the
        # next line.  This is preferable to making my line of code way too
        # long.

main()
