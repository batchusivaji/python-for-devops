"""Sum addition using nested loop."""

number = int(input("Enter a number: "))

while number > 9:
    RESULT = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        RESULT += digit
    number = RESULT

print("Final single digit sum =", number)

