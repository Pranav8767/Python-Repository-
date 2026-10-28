student=[]

while True:
    print("\n----College Records----")
    print("1.Add Student")
    print("2.delete Student")
    print("3.Search Student")
    print("4.Display Students")
    print("5.Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter name:")
        roll=int(input("enter rollno: "))
        marks=int(input("enter marks: "))

        student.append([name,roll,marks])
        print("added.")

    elif choice==2:
        roll=int(input("enter rollno to delete: "))

        found= False
        for st in student:
            if student[1]==roll:
                student.remove(st)
                found=True
                print("deleted")
                break
    elif choice==3:
        roll=int(input("enter roll no to search: "))

        found=False
        for st in student:
            if st[1]==roll:
                print("Name: ",st[0])
                print("Rollno: ",st[1])
                print("marks: ",st[2])
                found=True
                break
        if found==False:
            print("student not found")
