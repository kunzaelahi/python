# Input marks for English, Islamiat, and Maths out of 100
eng_marks = int(input("Enter marks for English: "))
isl_marks = int(input("Enter marks for Islamiat: "))
maths_marks = int(input("Enter marks for Maths: "))

# Total marks
total_marks = 300

# Calculate percentage
percentage = (eng_marks + isl_marks + maths_marks) / total_marks * 100

# Determine grade based on percentage using conditional statements
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Print percentage and grade
print("Percentage:", percentage)
print("Grade:", grade)







print("Twinkle, twinkle, little star,")
print("    How I wonder what you are!")
print("        Up above the world so high,")
print("        Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("    How I wonder what you are.")






# Accept two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum of the numbers
sum = num1 + num2

# Print the sum
print("Sum:", sum)






import sys

print("Python version:")
print(sys.version)




import datetime

# Get current date and time
current_date_time = datetime.datetime.now()

# Format the date and time as a string
formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the current date and time
print("Current Date and Time:", formatted_date_time)






# Accept marks for five subjects from the user
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))

# Calculate the total marks
total_marks = subject1 + subject2 + subject3 + subject4 + subject5

# Calculate the percentage
percentage = (total_marks / 500) * 100

# Determine grade based on percentage
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Generate the mark sheet
print("------ Mark Sheet ------")
print("Subject 1:", subject1)
print("Subject 2:", subject2)
print("Subject 3:", subject3)
print("Subject 4:", subject4)
print("Subject 5:", subject5)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)







# Accept the radius from the user
radius = float(input("Enter the radius of the circle: "))
pi=3.147
# Compute the area of the circle
area = pi * radius ** 2

# Display the computed area
print("The area of the circle is:", area)







# Accept the string from the user
string1 = input("Enter a Firstname: ")
string2 = input("Enter a Lastname: ")

# Reverse the string
reversed_string1 = " ".join(reversed(string1))
reversed_string2 = " ".join(reversed(string2))

# Print the reversed string
print("Reversed string:", reversed_string2,reversed_string1)




# Accept a number from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")