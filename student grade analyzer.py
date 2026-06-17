class Student:
    def __init__(self,name,marks):
        self.marks=marks
        self.name=name

    def average(self):
        s=sum(self.marks.values())
        n=len(self.marks)
        return round(s/n,2)
    
    def grade(self):
        avg=self.average()
        if avg>=80:
            return "A"
        elif avg>=60:
            return "B"
        elif avg>=50:
            return "C"
        elif avg>=40:
            return "D"
        else:
            return "F"
        
    def display(self):
        print(f"name:{self.name}")
        print("marks;")
        for sub,mark in self.marks.items():
            print(f"{sub}:{mark}")
        print(f"average:{self.average()}")
        print(f"grade:{self.grade()}")


class Classroom:
    def __init__(self):
        self.students=[]

    def add_student(self,student):
        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
           if student.name == name:
              self.students.remove(student)
              print(f"{name} removed successfully")
              return
    print(f"No student found")
        
        

    def showall(self):
        if len(self.students)==0:
            print("no student in classroom yet")
        else:
            for i in self.students:
               i.display()

    def top_student(self):
        top=self.students[0]
        for i in self.students:
            if i.average()>top.average():
                top=i
        return top
    
    def class_avg(self):
        c_avg=[]
        for i in self.students:
            c_avg.append(i.average())
        return (sum(c_avg)/len(c_avg))
    
    def rank_students(self):
       ranked = sorted(self.students, key=lambda s: s.average(), reverse=True)
       print("\n--- Student Rankings ---")
       for i, s in enumerate(ranked):
          print(f"Rank {i+1}: {s.name} — Average: {s.average()} — Grade: {s.grade()}")


        # FILE SAVING

import json 

def save_data(classroom,fh="students.json"):
    data={}
    for i in classroom.students:
        data[i.name]=i.marks
    with open(fh,"w")as f:
        json.dump(data,f)
    print("data saved successfully")

def load_data(fh="students.json"):
    try:
        with open(fh,"r") as f:
            d=json.load(f)
            c=Classroom()
            for n,m in d.items():
                c.add_student(Student(n,m))
            return c
    except FileNotFoundError:
        print("no saved data found . starting fresh")
        return Classroom()
        
        # MENU

def menu():
    classroom = load_data()   
    
    while True:
        print("\n--- Grade Analyzer ---")
        print("1. Add student")
        print("2. Remove student")
        print("3. Show all students")
        print("4. Top student")
        print("5. Class average")
        print("6. Rank students")
        print("7. Save and exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            name=input("enter name of the student:")
            marks={}
            n=int(input("enter the number of subjects:"))
            for i in range(n):
                sub=input(f"enter subject {i+1} name")
                m=int(input(f"enter marks of {sub}"))
                marks[sub]=m
            classroom.add_student(Student(name,marks))
            print(f"{name}added successfully")

        elif choice == "2":
            name=input("enter the nm=ame of the student to be removed")
            classroom.remove_student(name)
            print(f"{name} removed successfully")

        elif choice == "3":
            classroom.showall()

        elif choice=="4":
            top=classroom.top_student()
            print(f"top student:{top.name} with average:{top.average()}")

        elif choice=='5':
            print(f"class average:{classroom.class_avg()}")

        elif choice=='6':
            classroom.rank_students()

        elif choice=='7':
            save_data(classroom)
            break 
        else:
            print("invalid choice")

menu()

                    









        
                 
            

            

