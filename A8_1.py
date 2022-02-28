#Alexander Clifton
#2/27/2022

from importlib.machinery import all_suffixes

# Prompt the user for the name of the directory in which they want to save a file. - 15%
# Prompt the user for the name of the file they want to save to the directory in requirement 1. - 15%
# If the directory from requirement 1 doesn't exist the program must create the specified directory. - 20%
# The program will prompt the user for their name, address, and phone number and write that data as a line of comma separated values to the file using the directory and filename from requirements 1 and 2. (example: John Smith, 123 Main St,402-555-1212) - 20%
# After the data has been written to the file your program must open the file, read the contents, and display the contents to the user as program output. - 20%
# Create a GitHub Respository for Assignment 8.1 - 5%
# Submit a link to the respository from requirement 6 as your assignment submission. - 5%

#C:\Users\AlexC\OneDrive\Desktop\ProgrammingCourse

print("Welcome to Assignment A8.1")
direct = input("What is the directory you want to save a file to? :")
file = input("What is the file you want to save to the directory? :")

filepath =(f"{direct}\{file}")



def filewriting():
    with open(f"{file}.txt", 'a+') as newfile:
        name = input("What is your name? :")
        address = input("What is your address? :")
        phonenum = input("What is your phone number? :")
        newfile.write(name + ", ")
        newfile.write(address + ", ")
        newfile.write(phonenum + ", \n")
        
    with open(f"{file}.txt", 'r') as newfile:
        contents = newfile.read()
        print(contents)
filewriting()



