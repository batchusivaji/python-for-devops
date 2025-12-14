'''
Simple Intrest Calculation
'''

Principle_amount = float(input("Enter Pricipal amont: "))
Time            = float(input( "Enter Time: " ))
Rate_of_intrest = float(input( "Enter Intrest rate: " ))
Simple_Intrest  = ( Principle_amount * Time * Rate_of_intrest ) / 100
print(Simple_Intrest)
