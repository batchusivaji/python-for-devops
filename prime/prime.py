number = int(input("Enter a number:"))
index  = 2
is_prime = True

while index < number:
    remainder = number % index
    if remainder == 0:
        print(f"{number} is not prime")
        is_prime = False
        break
    index = index + 1
    
if is_prime:
     print(f"{number} is prime")