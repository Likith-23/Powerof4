#program to check if number is power of 4
def power_of4(number):
    count = 0
    #if only one set bit exists
    if (number & (~ (number & (number - 1)))):
        while (number > 1):
            number >>= 1
            count += 1
        #if ccount is even, return true else false
        if (count % 2 == 0):
            return True
        else:
            return False
number = int(input("Enter a number"))
if(power_of4(number)):
    print("NUMBER IS POWER OF 4...............................:)")
else:
    print("NUMBER IS NOT POWER OF 4.............................:)")