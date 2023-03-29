Deans_List = 3.5
Honor_Roll = 3.25
valid_grade = False

Last_name = input("Please enter last name \n")

while any(i.isdigit() for i in Last_name) :
    Last_name = input("The last name should be a string \n")

first_name = input("Please input first name \n")

while any(i.isdigit() for i in first_name) :
    first_name = input("The first name should be a string \n")

Grade = float(input("Please input grade \n"))
try:
    float(Grade)
except ValueError:
        
        Grade = float(input("grade should be a float number \n"))
    


while "ZZZ" not in Last_name:
    if Grade >= Deans_List:
        print("This student has made the Dean's list\n")
    elif Grade < Deans_List and Grade >= Honor_Roll:
        print("This student has made the honor roll\n")
    else:
        print("This student did not make the Dean's list or honor roll\n")
    Last_name = input("Please enter last name \n")
    while any(i.isdigit() for i in Last_name) :
        Last_name = input("The last name should be a string \n")
    if "ZZZ" in Last_name:
        break
    first_name = input("Please input first name \n")
    while any(i.isdigit() for i in Last_name) :
        Last_name = input("The last name should be a string \n")
    Grade = float(input("Please input grade \n"))