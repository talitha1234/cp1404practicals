"""
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # avoids possibility of ZeroDivision error
    while denominator == 0:
        print("Not a valid denominator. Cannot divide by 0.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions
# 1. ValueError will occur when string is entered as a denominator or numerator
# 2. ZeroDivisionError will occur when denominator entered is zero
# 3. Can avoid ZeroDivision error by using a while loop to check if denominator is zero
