#stripping a string 
#string has a built in function for removing extra spaces from the  edges string

string = input("please enter a string \n")
wordTobeReplaced=input(" please enter a word to be replace")
replaceWith = input(" please enter a word you want to replace in string\n")

##print(string.strip())

## removing a world from the string 
#we cant use two return in one funtion or we can?


def removeAword(string,wordTobeReplaced,replaceWith):
    newstring= string.replace(wordTobeReplaced,replaceWith)
    return newstring  


name= removeAword(string,wordTobeReplaced,replaceWith)
print(name)
