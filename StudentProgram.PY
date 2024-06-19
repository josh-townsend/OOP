import StudentClass as sc

id = 1101
name = 'john'
dob = '02/28/2001'
classification = 'junior'

student1 = sc.Student(id,name,dob,classification)

student1.calc_age()

student1.register()

print(f"Age is: {student1.get_age()}")
print(f"Student registers through: {student1.get_registration()}")

