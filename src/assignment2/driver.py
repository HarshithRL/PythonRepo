from src.assignment2.util import *

if __name__ == '__main__':
    Number_of_Record=int(input("Enter the number of record: "))
    Student_Records={}
    for i in range(Number_of_Record):
       name,*marks = input("Enter the name and Marks").split()
       Student_Records[name]=list(map(float,marks))
    Student=input("Enter the Name of Student to be Found")
avg_marks(Student_Records,Student)
