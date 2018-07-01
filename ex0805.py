#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
#Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

connection = open('mbox-short.txt') #make a connection to file
lines = connection.readlines() #read the file in, where each line is a string, making a list of strings
count = 0



for line in lines:
    if line.startswith("From "):
        line = line.rstrip()
        words = line.split()
        print(words[1])
        count = count + 1



print("There were", count, "lines in the file with From as the first word")
