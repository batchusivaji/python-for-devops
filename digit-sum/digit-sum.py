"""Sum addition using while loop."""

number = int(input("Enter a number:"))
RESULT = 0

while number > 0:
    digit  = number % 10
    number = number // 10
    RESULT = RESULT + digit
    if number == 0 and RESULT > 9:
        number = RESULT
        RESULT = 0

print(f"Number is: {RESULT}")
