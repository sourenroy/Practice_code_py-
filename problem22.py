marks1 = int(input("Enter Your marks :"))
marks2 = int(input("Enter Your marks :"))
marks3 = int(input("Enter Your marks :"))

total_marks = (100*(marks1 + marks3 + marks2))//300

if(total_marks >=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You're Pass",total_marks)

else:
    print("you fail Try next year ",total_marks)