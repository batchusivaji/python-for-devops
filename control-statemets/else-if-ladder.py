'''
A chain condtions executed from to bottom until one condition is True
if condition1:
   statement
elif condition2:
   statement
elif condition3:
   statement
else:
  statement
'''

marks = 62
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
