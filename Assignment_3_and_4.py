# 1. Write a Python program to print the following string in a specific format (see the
# output).

# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# Twinkle, twinkle, little star,
# How I wonder what you are




# print("Twinkle, twinkle, little star,")
# print("    How I wonder what you are!")
# print("        Up above the world so high,")
# print("        Like a diamond in the sky.")
# print("Twinkle, twinkle, little star,")
# print("    How I wonder what you are.")


# 2. Write a Python program to get the Python version you are using

# import sys

# print("Python version:")
# print(sys.version)


# 3. Write a Python program to display the current date and time.


# import datetime

# # Get current date and time
# current_date_time = datetime.datetime.now()

# # Format the date and time as a string
# formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

# # Print the current date and time
# print("Current Date and Time:", formatted_date_time)

# 4. Write a Python program which accepts the radius of a circle from the user and compute
# the area.


# # Accept the radius from the user
# radius = int(input("Enter the radius of the circle: "))
# pi=3.147
# # Compute the area of the circle
# area = pi * radius ** 2

# # Display the computed area
# print("The area of the circle is:", area)


# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# string1 = input("Enter a Firstname: ")
# string2 = input("Enter a Lastname: ")

# # Reverse the string
# reversed_string1 = " ".join(reversed(string1))
# reversed_string2 = " ".join(reversed(string2))

# # Print the reversed string
# print("Reversed string:", reversed_string2,reversed_string1)

# 6. Write a python program which takes two inputs from user and print them addition

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # Calculate the sum of the numbers
# sum = num1 + num2

# # Print the sum
# print("Sum:", sum)


# 7. Write a program which takes 5 inputs from user for different subject’s marks, total it
# and generate mark sheet using grades ?

# subject1 = float(input("Enter marks for subject 1: "))
# subject2 = float(input("Enter marks for subject 2: "))
# subject3 = float(input("Enter marks for subject 3: "))
# subject4 = float(input("Enter marks for subject 4: "))
# subject5 = float(input("Enter marks for subject 5: "))

# # Calculate the total marks
# total_marks = subject1 + subject2 + subject3 + subject4 + subject5

# # Calculate the percentage
# percentage = (total_marks / 500) * 100

# # Determine grade based on percentage
# if percentage >= 90:
#     grade = "A+"
# elif percentage >= 80:
#     grade = "A"
# elif percentage >= 70:
#     grade = "B"
# elif percentage >= 60:
#     grade = "C"
# elif percentage >= 50:
#     grade = "D"
# else:
#     grade = "Fail"

# # Generate the mark sheet
# print("------ Mark Sheet ------")
# print("Subject 1:", subject1)
# print("Subject 2:", subject2)
# print("Subject 3:", subject3)
# print("Subject 4:", subject4)
# print("Subject 5:", subject5)
# print("Total Marks:", total_marks)
# print("Percentage:", percentage)
# print("Grade:", grade)


# 8. Write a program which take input from user and identify that the given number is even
# or odd?

# number = int(input("Enter a number: "))

# # Check if the number is even or odd
# if number % 2 == 0:
#     print(number, "is an even number.")
# else:
#     print(number, "is an odd number.")

# 9. Write a program which print the length of the list?


# lst=[1,3,4,6,3]
# a=len(lst)
# print(a)


#10.Write a Python program to sum all the numeric items in a list?

# list1=[1, 5 , 4]
# sum=0
# for i in list1:
#     sum+=i

# print(sum)

# 11.Write a Python program to get the largest number from a numeric list.
# list2=[ 1,5,6,3,8]
# data=0
# for i in list2:
#     if data<=i:
#         data=i
# print(data)

# 12. Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.

# a=  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#    if i < 5:
#        print(i)








#Assignment 4
# 1. Make a calculator using Python with addition , subtraction ,
# multiplication ,division and power.

# val1 = int(input("val1 :"))
# val2 = int(input("val2 :"))
# op = input("enter your op:")

# if op == "+":
#     print("add values", val1 + val2)
# elif op == "-":
#     print("sub", val1 - val2)
# elif op == "*":
#     print("multiplt", val1 * val2)
# elif op == "/":
#     print("div", val1 / val2)
# else:
#     print("error")


# 2. Write a program to check if there is any numeric value in list using for loop.

# my_list = ["apple", 3, "banana", 5.6, "orange"]

# # Initialize a flag variable to False
# has_numeric = False

# # Loop through the list
# for item in my_list:
#   # Check if the item is a numeric value (int or float)
#   if isinstance(item, (int, float)):
#     # Set the flag to True and break the loop
#     has_numeric = True
#     break

# # Print the result
# if has_numeric:
#   print("The list has a numeric value.")
# else:
#   print("The list has no numeric value.")


#   3. Write a Python script to add a key to a dictionary.

# my_dict = {"name": "Ali", "age": 25, "city": "Karachi"}

# # Print the original dictionary
# print("The original dictionary is", my_dict)

# # Define a new key and value to add
# new_key = "country"
# new_value = "Pakistan"

# # Add the new key and value to the dictionary
# my_dict[new_key] = new_value

# # Print the updated dictionary
# print("The updated dictionary is", my_dict)

# 4. Write a Python program to sum all the numeric items in a dictionary.

# my_dict = {"name": "Ali", "age": 25, "city": "Karachi", "salary": 50000, "country": "Pakistan"}

# # Initialize a sum variable to zero
# total = 0

# # Loop through the dictionary values
# for value in my_dict.values():
#   # Check if the value is a numeric value (int or float)
#   if isinstance(value, (int, float)):
#     # Add the value to the sum
#     total += value

# # Print the result
# print("The sum of all the numeric items in the dictionary is", total)


#5. Write a program to identify duplicate values from list.
# lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
 
# uniqueList = []
# duplicateList = []
 
# for i in lis:
#     if i not in uniqueList:
#         uniqueList.append(i)
#     elif i not in duplicateList:
#         duplicateList.append(i)
 
# print(duplicateList)


# 6. Write a Python script to check if a given key already exists in a dictionary
# my_dict = {"name": "Ali", "age": 25, "city": "Karachi"}

# # Define a key to check
# key = "age"

# # Check if the key is in the dictionary using the in operator
# if key in my_dict:
#   print("The key", key, "already exists in the dictionary.")
# else:
#   print("The key", key, "does not exist in the dictionary.")