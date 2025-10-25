number = int(input("Enter a number: "))
index = 2

print(f"Factors of {number} are:")

while index <= number:
    if number % index == 0:
        print(index)
    index = index + 1





