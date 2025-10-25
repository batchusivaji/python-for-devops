number = int(input("Enter a number: "))
result = 0
originalNumber = number

while number > 0:
     digit  = number % 10
     number = number // 10
     result = result * 10 + digit
   
if originalNumber == result:
     print("say Pallendrome")
else:
   print("say not Pallendrome")

