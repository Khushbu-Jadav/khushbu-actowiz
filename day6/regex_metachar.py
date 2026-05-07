import re

b="khushbujadavactowiz@gmail.com"


#search method gives the index of pattern's first occurence
#the "r" in the beginning is making sure that the string is being treated as a "raw string"

match=re.search(r".",b) # . gives any char
match2=re.search(r"\.",b) # (escape)\. gives actual .
match3=re.search(r"[@]",b)

print(match)
print(match2)
print(match3)

#findall Returns a list containing all matches
match4=re.findall(r"[a]",b) # Match any one character from a set
# findall Return ALL matches
match5=re.findall(r"[abc]",b)

print(match4)
print(match5)


text="cat cot cut"
print(re.findall("c[ao]t", text))

text2="a b c d e x y z"
print(re.findall("[a-d]",text2)) #A set of characters

#special shortcuts
# \d : digit
# \d+ : multiple digits in one element
# \w : word char
# \s : space

text3="the number is 5026"
print(re.findall(r"\d",text3))

print(re.findall(r"\d+",text3))

print(re.findall(r"\w",text3))

print(re.findall(r"\s",text3))

print("\n")

# + One or more occurrences
text4 = "aaa a aa"
print(re.findall("a", text4))
print(re.findall("a+", text4))

# * Zero or more occurrences
text5 = "aa ab a"
print(re.findall("a*", text5))


# string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain 25"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

print(re.findall(r"[a-n]", txt)) #A set of characters
print(re.findall(r"\d", txt)) #Signals a special sequence (can also be used to escape special characters)
print(re.findall(r"he..o", "hello world")) # . Any character (except newline character)
print(re.findall(r"^T",txt))

#Split Returns a list where the string has been split at each match
#split the string at every white-space character
y=re.split(r"\s",txt)
print(y)
print(re.split(r"\s",txt,1))

#sub Replaces one or many matches with a string
#Replace all white-space characters with the digit "4"
z = re.sub(r"\s", "4", txt)
print(z)

#? 0 or 1 occurence
print(re.findall("he.?o","hello"))
#there are two char between "he" and "o" which are "ll" ,so no match
print(re.findall("T.?e",txt))

#{} Exactly the specified number of occurrences
print(re.findall(r"he.{2}o","hello"))

#| Either or
print(re.findall(r"India|Spain",txt))


#flags

txt2 = "Åland"
#re.ASCII or re.A Returns only ASCII matches
#without flag, it would return all character
print(re.findall(r"\w",txt2))
print(re.findall(r"\w",txt2,re.ASCII))
#short way
print(re.findall(r"\w",txt2,re.A))
print("\n")

#re.DEBUG Returns debug information
print(re.findall(r"spain",txt, re.DEBUG))
print('\n')

#re.DOTALL / re.S : Makes the . character match all characters (including newline character)
name="""hi
my
name
is
khushbu"""
print(re.findall("me.is",name,re.DOTALL))
print(re.findall("me.is",name)) #only . not contains the \n
print(re.findall("me.is",name,re.S))
print('\n')

#re.IGNORECASE / re.I : Case-insensitive matching
print(re.findall("spain", txt, re.IGNORECASE))
print(re.findall("spain", txt, re.I))
print(re.findall("spain", txt))
print("\n")

#re.MULTILINE / re.M : Returns matches at the start/end of each line
txt3="""There
aint much
rain in 
Spain"""
print(re.findall("^ain",txt3))
print(re.findall("^ain",txt3,re.MULTILINE))
print(re.findall("^ain",txt3,re.M))
print('\n')
#re.NOFLAG : Specifies that no flag is set for this pattern

txt4="Åland"
#re.UNICODE / re.U :  Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches
print(re.findall(r"\w", txt4, re.UNICODE))
print(re.findall(r"\w", txt4, re.U))
print(re.findall(r"\w", txt4))
print(re.match(r"\u0047", "G"))
print(re.match(r"\u0047", "G"))

#re.VERBOSE / re.X : Allows whitespaces and comments inside patterns. Makes the pattern more readable
text = "The rain in Spain falls mainly on the plain"
pattern = """
[A-Za-z]* #starts with any letter
ain+      #contains 'ain'
[a-z]*    #followed by any small letter
"""
print(re.findall(pattern, text, re.VERBOSE))
print(re.findall(pattern, text))
print(re.findall(pattern, text, re.X))
print('\n')

#Special Sequences
#\A	: Returns a match if the specified characters are at the beginning of the string
print(re.findall(r"\AThe", text))
print(re.findall(r"\bain", text)) #for checking in beginning word
#no word is starting from ain ,so []
print(re.findall(r"ain\b", text)) #for checking at end word
#Returns a match where the specified characters are
#present, but NOT at the beginning
print(re.findall(r"\Bain", text))
#present, but Not at the end of a word
print(re.findall(r"ain\B", text))
#\d: Returns a match where the string contains digits (numbers from 0-9)
print(re.findall(r"\d",text))
#\D: Returns a match where the string DOES NOT contain digits
print(re.findall(r"\D", text))
#\s: Returns a match where the string contains a white space character
print(re.findall(r"\s", text))
#\S: Returns a match where the string DOES NOT contain a white space character
print(re.findall(r"\S",text))