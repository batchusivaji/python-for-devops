'''
An if inside another if
if condition:
    executes when first condtion is true
    if condition:
     executes block when second condtion is true
   
'''

# marks = 45
# if marks>=0 and marks<=100:
#     if marks>40:
#         print("you passed the exam")
# 
# 
marks = 85
income= 90000
if marks > 75:
    if income <80000:
        print("eligible for scholarship")
    else:
       print("Not eligible for scholarship due to high income") 
   
   