fname = input("Please enter file name:")
fconnection = open(fname)
num_lines = 0
Conf_count = 0
for eachline in fconnection:
    if not eachline.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        num_lines = num_lines + 1
        Conf_count  = Conf_count + float( eachline[-6:])

conf_average = Conf_count / num_lines

print("Average spam confidence:", conf_average)
