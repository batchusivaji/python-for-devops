# """Find out the LCM of numbers from 1 to NUMBER."""
# 
# NUMBER = int(input("Enter a number: "))    # You can enter any number 
# MULTIPLE = 1      # Start with 1
# i = 1             # Counter
# 
# while i <= NUMBER:
#     # Find GCD of MULTIPLE and i without using functions
#     a = MULTIPLE
#     b = i
#     while b != 0:
#         TEMP = b
#         b = a % b
#         a = TEMP
#     gcd = a
# 
#     # Calculate LCM using GCD
#     MULTIPLE = MULTIPLE * i // gcd
#     i += 1
# 
# print("Smallest number divisible by 1 to", NUMBER, "is:", MULTIPLE)


# NUMBER = int(input("Enter a number: "))
# MULTIPLE = 1
# i = 1

# while i <= NUMBER:
#     a = MULTIPLE
#     b = i

#     # Correct GCD calculation
#     while b != 0:
#         a, b = b, a % b
#     gcd = a

#     MULTIPLE = MULTIPLE * i // gcd
#     i += 1

# print("LCM of numbers from 1 to", NUMBER, "is", MULTIPLE)


number = int(input("Enter a number: "))
mul = 1   # Start with 1

for index in range(1, number + 1):      # Loop from 1 to 'number'
    a = mul                             # Current LCM so far
    b = index                           # Current number to include

    # Find GCD of a and b
    while b != 0:
        temp = b                        # Store b temporarily
        b = a % b                       # b becomes remainder of a divided by b
        a = temp                        # a takes old b's value

    gcd = a                             # When b=0, a is GCD

    # Calculate LCM using formula
    mul = mul * index // gcd

print("Smallest number divisible by 1 to", number, "is:", mul)
