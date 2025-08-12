num1_string =input("Enter the first number")
num2_string =input("Enter the second number")
operation =input("Enter the operation(+.-,*,/):")
#Convert the string to numbers
num1=float(num1_string)
num2=float(num2_string)
#Perform the calculation based on the operation
if operation =='+':
    result =num1+num2
elif operation =='-':
    result =num1-num2  
elif operation =='*':
    result =num1*num2
elif operation =='/':
    result =num1/num2
else:
 print =(" divide by zero.") 
print("valid operations")
# Print the result
print(f"{num1}{operation}{num2}={result}") 

