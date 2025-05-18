# 1. Write a script to calculate the area and perimeter of a rectangle using variables. 
l= int(input("l:"))
b= int(input("b:"))
print(f"Area of rectangle is {l*b} units.")
print(f"Perimeter of recatngle is {2*(l+b)} units.")

# 2. Write a script that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number. 
num1= int(input("num1:"))
num2= int(input("num2:"))
if(num1==num2):
    print("Both the numbers are equal.")
elif(num1>num2):
    print("Num1 is greater than Num2.")
elif(num1<num2):
    print("Num1 is less than Num2.")

# 3. Write a script that checks if a given year is a leap year (divisible by 4, but not by 100 unless also divisible by 400). 
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
 print(f"{year} is not a leap year.")

# 4. Experiment with different arithmetic and logical operators in the interpreter.
print("ARITHMATIC OPERATOR")
a =int(input("a:"))
b= int(input("b:"))
print(a+b)  #Addition
print(a-b)  #Subtraction
print(a*b)  #Multiplication
print(a/b)  #Division
print(a**b) #Exponent
print(a//b) #Modulus Divsion
print(a%b)  #Modulo

print("LOGICAL OPERATOR")
print("OR OPERATOR:")
c=6
print(c<7 or c>10) #If one condition satisfies from both the condition then it's true, it fails only when both the condition are false.
print("AND OPERATOR:")
c=6
print(c<7 and c>10) #Only true when both the condition are true, otherwise false.
print("NOT OPERATOR:")
c=6
print(not(c<7)) #If true then false and false then true.

# 5. Write a script that concatenates two strings and prints the result.
def concatenation():
   s1= "TECHSONIX "
   s2= "SOLUTIONS"
   print(s1 + s2)
concatenation()