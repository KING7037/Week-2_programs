number_of_Students = int(input("Enter number of students"))
number_of_Size = int(input("Enter number of required group size"))
count = 0
adding_number_of_Size = 0
remaining_Students = 0

while number_of_Students >= adding_number_of_Size:
    adding_number_of_Size = number_of_Size + adding_number_of_Size
    count = count + 1
remaining_Students = adding_number_of_Size - number_of_Students
print(remaining_Students)
print(count)
    
