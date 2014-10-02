# Regular expressions activity I
# Learning about regular expressions (patterns).

# The import statement below tells Python to load a
# set of 'regular expression' functions.  If you use
# regular expressions in your programs, you NEED
# to have this line.
import re

def main():
    name = raw_input("What's your first name? ")
    poem = bananaFana(name.strip())
    print "\n" + poem
    print "\n  (This poem has %d characters in it)" % len(poem)

def bananaFana(name):
    '''Given a name (string), returns a rhyme (string).'''
    name = name.lower()
    first_letter = name[0]
    if isVowelRegEx(first_letter):
        suffix = name
    else:
        suffix = name[1:len(name)]

    rhyme = name + ' ' + name + ' bo-b' + suffix + '\n'
    rhyme = rhyme + 'banana-fana fo-f' + suffix + ' ---\n'
    rhyme = rhyme + 'me my mo m' + suffix + '\n'
    rhyme = rhyme + name + '!'
    return rhyme

def isVowel(character):
    '''Returns True if character is a lowercase vowel and False otherwise.'''
    if ((character == 'a') or
        (character == 'e') or
        (character == 'i') or
        (character == 'o') or
        (character == 'u')):
        return True
    return False

def isVowelRegEx(character):
    '''Returns True if character is a lowercase vowel and False otherwise.'''
    # re.match(pattern, string) returns None if no match is found
    if re.match('^[aeiou]$', character) == None:
        return False
    return True

main()
