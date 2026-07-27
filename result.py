print("***********STUDENT REPORT CARD***************")

name = input("Enter student's name:-")

english = int(input("enter your english marks:" ))
maths = int(input("enter your maths marks:" ))
sst = int(input("enter your S.st marks:" ))
hindi = int(input("enter your hindi marks:" ))
science= int(input("enter your Science marks:" ))
total= english + maths + sst + science + hindi 


percentage= (total/500*100)

if percentage>=90:
     print("You got A grade")
    
elif percentage>=75:
     print("You got B grade")
    
elif percentage>=60:
     print("You got C grade")
    
elif percentage>=40:
     print("You got D grade")


else:
     print("sorry you failed the exam please try again!")


print(f"student name:-{name}")
print(f"percentage:{percentage:.2f}%")
print(f"Total marks:- {total}")

    





