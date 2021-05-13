number= int( input("  "))
if number%400==0:
    print("True")
elif number%100==0:
    print("False")
elif number%4==0:
    print("True")
else:
    print("False")
