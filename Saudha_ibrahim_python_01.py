# Name: Saudha Ibrahim

# Course: ICT and python programming


# PYTHON VARIABLES AND DATA TYPES


#Q1--Declare and initialize two variables, num1 and num2, with integer values. Calculate and print their sum. 


num1= 75
num2=25

result=num1+num2

print("the total sum of num1 and num2 is:",result)


#Q2--Create a variable, message, and assign it a string value. Append another string," World!", to it and print the result. 


message="My"

message="My "+"World!"

print(message)


#Q3--Define a variable, is_python_fun, and assign it a boolean value. Print a statement based on whether Python is considered fun. 


is_python_fun = True  

if is_python_fun:
    
    print("yes, it is fun")
else:
    print("no, its absolutely not fun")
  
      
    #Q4--Create a list, fruits, with three different fruit names. Print the list and then add a new fruit to it. Print the updated list.
    

fruits=["Guava","kiwi", "Peach"] 
  
print("fruits_list_01=",fruits)
  
fruits.append("Orange") 
  
print("fruits_list_02=", fruits)


#Q5--Declare a variable, price, with a floating-point value. Convert it to an integer and print both the original and converted values


price=(80.75)

print("Original Value:", price,"/-rs only")

converted_price= int(80.75)

print("Converted Value: ", converted_price,"/-rs only")


#Q6--Create a dictionary, student_info, with keys for 'name', 'age', and 'grade'. Assign corresponding values and print the dictionary.


student_info={"Name":"Sakina Ibrahim",
"Age":15, "grade":"B+"}

print("student_info=", student_info)

age = int(input("Kindly, enter your age: "))

if age <= 12:
    print("According to your age, you are a child.")

elif age <= 19:
    print("According to your age, you are a teenager.")

else:
    print("According to your age, you are an adult.")
       

#Q7--Combine two strings using string concatenation, and then use string interpolation to include the length of the resulting string in a print statement.
  

my_dept= "Anesthesia and Critical care Sciences "

at= "at"

my_institute=" Sims-Siut."

i_am_studying= my_dept + at +  my_institute

print("I am studying", i_am_studying)

length_of_statement= len(i_am_studying)

print(f"The length of above statement is {length_of_statement} characters.")


#Q8=Create a tuple, days_of_week, with the names of the days. Access and print the third day of the week.


days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print("Days of the week:", days_of_the_week)

third_day = days_of_the_week[2]

print("The third day of the week is", third_day,)


