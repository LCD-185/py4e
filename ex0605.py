#Assignment 6.5

text = "X-DSPAM-Confidence:    0.8475";
length = len(text)
num_ind = text.find('0')

number = float( text[num_ind +1:] )

print(number)
