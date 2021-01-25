#Bond present value calculator
#Kenneth Burchfiel
#First published on 2021-1-25
#Professor Anton Lines's slides and Excel example were useful for building and revising this code
#Use at your own risk! I did some basic review of the code but I can't guarantee that the present value returned by the code is accurate, especially because the code features minimal error checking. In addition, results may be slightly inaccurate (e.g. 99.99999999999997 instead of 100) due to how computers process numbers.

def calcbondpv(facevalue,yearstomaturity,coupon,compoundrate,yieldtomaturity): 
    pv = 0
    yieldtomaturity /= 100 #Converts the yield from a percentage figure to a decimal
    couponamount = (facevalue*coupon/100)/compoundrate #Calculates the value of each coupon payment
    for i in range (1,(yearstomaturity*compoundrate)+1): #Calculates value of coupon payments
        pv += couponamount/(1+yieldtomaturity/compoundrate)**(i)
        #print("at the end of period",i,"pv is now",pv,"most recent value added to pv was",couponamount/(1+yieldtomaturity/compoundrate)**(i)) #Helpful for debugging
    pv += facevalue/(1+yieldtomaturity/compoundrate)**(compoundrate*yearstomaturity) #Adds the discounted value of the bond's face value to the value of its coupon payments
    #print("discounted face value added to pv is",facevalue/(1+yieldtomaturity/compoundrate)**(compoundrate*yearstomaturity)) #Also helpful for debugging
    return pv

while(True): #Infinite loop, which the user can exit by closing the console/terminal
    inputs = (input("Welcome to the Bond Present Value Calculator!\nEnter the following parameters separated by spaces:\n1. The face value of the bond.\n2. Its years to maturity (in integer form).\n3. Its annual coupon rate (as a percentage but without the percentage symbol). \n4. The annual compound rate (e.g. 2 for a bond with semiannual compounding, or 1 for a bond with annual compounding).\n5. Its yield to maturity (also as a percentage but without the percentage symbol).\nFor an example, enter \"example\". "))
    if (inputs.lower() == "example"):
        print("\nExample: To calculate the pv of a bond with $100 face value, 20 years to maturity, a 2.5 percent annual coupon rate, semiannual compounding, and a 1.7 percent yield to maturity, enter 100 20 2.5 2 1.7.\n") #If the user inputs "example", the program will then return to the "Enter the following parameters . . . " dialog.
    else:
        arguments = inputs.split() #Takes the one-line input from the user and converts it into a list of arguments, each of which can be modified and assigned a variable name
        facevalue=float(arguments[0])
        yearstomaturity=int(arguments[1])
        coupon=float(arguments[2])
        compoundrate=int(arguments[3])
        if compoundrate==0:
            print("Compound rate cannot be 0. Please enter a compound rate of 1 for a bond with annual compounding.")
            continue #restarts while loop from the beginning
        yieldtomaturity=float(arguments[4])
        print(f"Face value: {facevalue} Years to maturity: {yearstomaturity} Coupon: {coupon} Number of coupon payments per year: {compoundrate} Yield to maturity: {yieldtomaturity}")
        print(f"Bond present value: {calcbondpv(facevalue,yearstomaturity,coupon,compoundrate,yieldtomaturity)}\n")
        










