#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.


# This code works but will not get you the marks because the markers want you to use a for loop and append()

connection = open('romeo.txt') #open a connection to romeo.txt
romeo = connection.read() #read the whole file as one string
words = romeo.split() # split this string into individual words
unique = list ( set(words) )#use set function to remove duplicated words
unique.sort() #sort this list 'unique'
print(unique)


#This correct and will get you the marks

connection = open('romeo.txt') #open a connection to romeo.txt
romeo = connection.read() #read the whole file as one string
words = romeo.split() # split this string into individual words
unique = list()   #a list of unique words, initally empty

for word in words :
    if word not in unique :
        unique.append(word)

unique.sort()
print(unique)
