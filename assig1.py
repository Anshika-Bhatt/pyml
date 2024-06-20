# 1. Write a program that takes two numbers as input and prints their sum.
a=int(input("enter number 1-"))
b=int(input("enter number 2-"))
sum=a+b
print("the sum of the numbers is",sum)

# 2. Write a python program that checks whether a given number is even or odd.
num=int(input("enter the number-"))
if num>0:
    print("the number is positive")
elif num==0:
    print("zero is neither positive nor negative")
else:
    print("the number is negative")

# 3. Write a python program that calculates the factorial of a given number.
num1=int(input("enter a number-"))
fact=1
for i in range(1,num1+1):
    fact*=i
print("the factorial of the given number is",fact)

# 4. Write a program that asks the user for their name and then prints a greeting message.
name=input("enter your name-")
print("Hello!",name,)

# 5. Write a program that takes a string input from the user and writes it to a text file.

str = input("Please enter a string: ")
f = "user_input.txt"
with open(f, 'w') as file:
    file.write(str)
print(f"The string has been written to {f}")


# 6. Write a program that reads the content of a text file and prints it to the console
f = "user_input.txt"
try:
    with open(f, 'r') as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"The file {f} does not exist.")

# 7. Write a python program that takes a string as input and returns its length.
str=input("enter a string to find its length-")
print(len(str))

# 8. Write a python program that concatenates two strings and returns the result.
str1=input("enter first string-")
str2=input("enter second string-")
rstr=str1+str2
print(rstr)

# 9. Write a python program that checks if a substring is present in a given string.
str3=input("enter a string-")
substr=input("enter the substring to be checked-")
if substr in str3:
    print("yes!",substr,"found in",str3)
else:
    print("no!",substr,"not found in",str3)

# 10. Write a python program that converts a given string to uppercase.
str4=input("enter the string-")
print(str4.upper())

# 11. Write a python program that generates the first n numbers in the Fibonacci sequence
def fibo(n):
    if n>0:
        if n==0:
            print("enter value of n more than 0")
        elif n==1:
            return 0
        elif n==2:
            return 1
        else:
            return fibo(n-1)+fibo(n-2)
        
n=int(input("enter a number-"))
for i in range(1,n+1):
    print(fibo(i),end=" ")

# 12. Write a python program that calculates the sum of the digits of a given number.
num2=int(input("enter a number-"))
sum1=0
while num2>0 :
    sum1+=(num2%10)
    num2//=10
print("the sum of digits is",sum1)

# 13. Write a program that asks the user for their birth year and calculates their age.
pr_year=int(input("enter present year-"))
doy=int(input("enter your birth year-"))
if pr_year>doy:
    age=pr_year-doy
    print("your age is",age)
else:
    print("invalid input")

# 14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
l = []
print("Enter multiple lines of text (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    l.append(line)

print("\nYou entered:")
for line in l:
    print(line)

# 15. Write a program that reads data from a CSV file and prints it to the console.
import csv
filename = "data.csv"

try:
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f"The file {filename} does not exist.")


# 16. Write a program in python that counts the frequency of each character in a string.
def countfreq(str):
    fr = {}
    for ch in str:
        if char in fr:
            fr[ch] += 1
        else:
            fr[ch] = 1
    return fr
string = input("Please enter a string: ")
fr= countfreq(string)
print("Character frequency:")
for char, count in fr.items():
    print(f"'{char}': {count}")


# 17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
str4=input("enter the string to print in title case-")
print(str4,"in title case is",str4.title())

# 18. Write a python program that checks if two strings are anagrams of each other
def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

string1 = input("Please enter the first string: ")
string2 = input("Please enter the second string: ")

if anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')

# 19. Write a python program that removes all punctuation from a given string.
str5=input("enter a string-")
newstr5=""
for i in range(len(str5)):
    if str5[i] not in ["!",".",",",";",":","?","-",'"',"'"]:
        newstr5+=str5[i]
print(newstr5)

# 20. Write a python program that takes a list of numbers and returns their sum.
n=int(input("how many numbers do you want to sum?"))
list=[]
for i in range(n):
    j=int(input("enter number-"))
    list.append(j)
print("sum of the numbers is",sum(list))

# 21. Write a python program that counts the occurrences of a specific element in a list
n=int(input("how many elements you want in the list?"))
list1=[]
for i in range(n):
    j=int(input("enter the number-"))
    list1.append(j)
ele=int(input("enter the number whose occurences needs to be counted-"))
print(ele,"occurs",list1.count(ele),"times in the list")

# 22. Write a python program that returns the minimum and maximum values in a list of numbers.
num5=int(input("how many numbers you want to enter?"))
list1=[]
for i in range(num5):
    j=int(input("enter the number-"))
    list1.append(j)
print("the minimum is",min(list1),"and the maximum is",max(list1))

# 23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def main():
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose the conversion type (1 or 2): ")
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")
if __name__ == "__main__":
    main()

# 24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
a=int(input("enter first number-"))
b=int(input("enter second number-"))
c=input("enter the operation to enter->+,-,/,*: ")
if c=="+":
    print(a+b) 
elif c=="-":
    print(a-b)
elif c=="/":
    print(a/b)
else:
    print(a*b)

# 25. Write a program that copies the contents of one text file to another.
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        
        with open(destination_file, 'w') as dest:
            dest.write(content)
        
        print(f"Contents of {source_file} have been copied to {destination_file}.")
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
str6=input("enter the string-")
c=input("enter P/p for prefix and S/s for suffix-")
if c=="P"or "p":
    s=input("enter the prefix-")
    print(str6.startswith(s))
else:
    s=input("enter the suffix-")
    print(str6.endswith(s))

# 27. Write a program in python that converts a string into a list of its characters
str=input("enter the desired string-")
list=list(str)
print(list)