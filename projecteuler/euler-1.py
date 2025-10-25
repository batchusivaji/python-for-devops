result = 0
index  = 2
max    = int(input("Eneter a number:"))

while index < max:
    if (index%3==0) or (index%5==0):
        result = result + index
    index = index + 1

print(f"sum is:{result}")