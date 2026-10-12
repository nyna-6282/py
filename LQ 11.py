def div():
    try:
        numerator=float(input("ENTER THE NUMERATOR : "))
        denominator=float(input("ENTER THE DENOMINATOR : "))
        result=numerator/denominator
        print("Result : ",result)
    except ZeroDivisionError :
        print("ERROR : DIVISION BY ZERO IS NOT ALLOWED ..")
div()
