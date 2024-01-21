import os

def main():
    number = int(input("\nHow many studs? "))
    metres = m(number)
    kms = km(metres)
    miles = mi(kms)
    print("That's", metres, "m.")
    print("That's", kms, "km.")
    print("That's", miles, "mi.")

def m(number):
    metres = round(int(number) * 0.28, 2)
    return metres

def km(metres):
    kms = round(metres / 1000, 2)
    return kms

def mi(kms):
    miles = round(kms / 1.60934, 2)
    return miles

while True:
    main()
