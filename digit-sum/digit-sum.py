number = int(input("Enter a number:"))
result = 0
while number > 0:
    digit  = number % 10
    number = number // 10
    result = result + digit
if number > 9:
    number = result
    result = 0
print(f"Number is: {result}")
