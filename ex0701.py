fname = input("Enter file name:")
connection = open(fname)

text = connection.read()
upText = text.upper()
upText = rstrip(upText)

print(upText)
