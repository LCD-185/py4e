def computepay(h,r):
    if h <= 40 :
        pay = h*r
    elif h > 40 :
        overtime = h-40
        pay = 40*r + overtime*1.5*r
    return(pay)


hrs = input("Enter Hours:")
rate = input("Enter rate:")

try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("Please enter numbers")
    quit()

pay  = computepay(hrs, rate)
print (pay)
