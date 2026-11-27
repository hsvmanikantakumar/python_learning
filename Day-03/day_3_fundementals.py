students_list=["mani","venkatesh","Balaji","gopi","Nanda"]
print(students_list)


Bsc_students_list=["mani","venkatesh",["balaji","gopi","nanda"]]
print(Bsc_students_list)
print(type(Bsc_students_list))
print(id(Bsc_students_list))

Bsc_students_list.append("Ram")
print(Bsc_students_list)
print(type(Bsc_students_list))
print(id(Bsc_students_list))

college_details=("manikanta",19,"chaitanya bharathi degree college","B.Sc computer science")
print(college_details)
print(type(college_details))
print(id(college_details))



students_dictonary={
        "Name" : "mani",
        "age" : 19,
        "college" : "chaitanya bharathi degree college",
        "city" : "chirala"
}
print(students_dictonary)


products_set={"laptop","mouse","keyboard",}
print(products_set)

products_set={"laptop","mouse","keyboard","laptop","pc"}
print(products_set)



z=4+9j
print(z)
print(z.real)
print(z.imag)
print(type(z))
print(id(z))



x=1
print(x)
print(type(x))
print(id(x))
y=0
print(y)
print(type(y))
print(id(y))

x=bool(x)
y=bool(y)
print(x)
print(type(x))
print(id(x))
print(y)
print(type(y))
print(id(y))




Rollno_25020={
               "student_name" : "mani",
               "Age" : 19 ,
               "percentage" : 97.5 ,
               "pass" : "True" ,
               "college_deails" :("Chaitanya Bharathi Degree college","chirala"),
               "subjects" :["OOPs Through JAVA","DataBase Management System","Computer Organisation"]
}
print(Rollno_25020)
print(type(Rollno_25020))
print(Rollno_25020["student_name"])
print(Rollno_25020["subjects"])