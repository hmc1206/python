#출석번호가 앞에 100을 붙이기로함
students = [1,2,3,4,5,]
print(students)
students = [i+100 for i in students]
print(students)

students = ["iron man","thor","i am groot"]
students = [len(i) for i in students]
print(students)
students = ["iron man","thor","i am groot"]
students = [i.upper() for i in students]
print(students)