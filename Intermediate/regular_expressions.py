### Regular Expressions ###

import re

regex = r'[lL]ike'
str = 'I like Python'

# match: searches only in the beginning of the first line of the 
# string and returns matched objects if found, else returns None.

match = re.match(regex, str)
try:
    span_match = match.span()
    print(span_match)
except:
    print(match)

# search: Returns a match object if there is one 
# anywhere in the string, including multiline strings.
search = re.search(regex, str)
print(search)


# findall: Returns a list containing all matches
findall = re.findall(regex, str)
print(findall)

# split: Takes a string, splits it at the match points, returns a list
print(re.split('e', str))

# sup: Replaces one or many matches within a string

str = '^I~^~ ~~l~^~ik~~e ~^~Py~~th^~~on & ^I Li~~k^e G~~i~^~t^Kr~~ak~^~e^n^'
print(re.sub('[~^]','', str))

# patterns

rex = r'[a].+'
str = 'Quiero entender este tema hoy y acabar el curso de Python a lo que sea'

print(re.findall(rex,str))