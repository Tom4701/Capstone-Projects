import math

option = "Please select investment or bond: \n"
option = input(option)

if ( option == 'investment'):
    p = float(input("Enter the amount you are depositing: "))
    i = float(input("Enter the interest rate (without the %): "))
    t = float(input("Enter the length of the investment (years): "))
    interest = str(input("Choose either 'Simple' or 'Compound' interest: ")).lower()
    if (interest == 'simple'):
                  r = i/100
                  a = p*(1+r*t)
                  print("Your new Total is: ",a)
    if (interest == 'compound'):
                  r = i/100
                  a = p*math.pow((1+r),t)
                  print("Your new Total is: ",a)
    if (interest != 'simple' and interest != 'compound'):
          print("Invalid option!")

#Bond Option, get input from user, calclate monthly repayment value and display

if ( option == 'bond'):
    p = float(input("Enter the present value of the house: "))
    i = float(input("Enter the interest rate (without the %): "))
    n = float(input("Number of months planned to repay the bond: "))
    r = i/100/12
    x = (r*p)/(1-math.pow((1+r),(-n)))
    print("Your total payable each month is: ",x)
