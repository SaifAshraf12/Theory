# make and display Dictionary
student ={
    'name':'saif ashraf',
    'roll #':'SP24-BBA-099',
    'section':'C',
    'program':'BBA',
    'department':'Management Sciences',
    'age':20,
    'contact #':3124134282,
    'email':'saifashraf@gmail.com',
    'city':'Muridke',
    'religion':'Islam'
    }
print(student)
print(type(student)) # displays class of variable

# accessing values of dictionary through keys
print(student['email'])
print(student['name'])
print(f'student email is {student["email"]}')
print(f'student religion is {student["religion"]}')

# accessing values by assigning key's value to a variable
student_age = student['age']
print(student_age)
student_city = student['city']
print(f'student lives in city {student_city}')

# accessing values by using get()
print(student.get('section'))
print(f'student department is {student.get("department")}')
student_age = student.get('age')
print(f'student is {student_age} years old')
print(f'student uses university transport services to come from {student.get("city")}')
# if key does not exist in dictionry
print(f"student is citizen of country: {student.get('country','country does not exist')}")

# adding new keys in dictionary
student['country'] = 'pakistan'
student['gpa'] = 3
print(student)

# modifying key values
student['gpa'] = 3.1
student['section'] = 'B'
print(student) # if key already exists in dictionary then itsvalue will be modifies otherwise new key will be added in dictionary
print(f"stdent gpa is now {student['gpa']}")
print(f"student section is now {student['section']}")

# removing key value pairs in dictionary
del student['religion']
print(student)

# title() display te value of key like get() 
print(student['country'].title())
student_roll = student['roll #'].title()
print(f'student roll # is {student_roll}')

# items() to display all key and value pairs of dictionary
all_items = student.items()
print(f'all_items in dictionary are {all_items}')
# iteration through item() to display all key value pairs within a dictonary
for key,value in student.items():
    print(f'key:{key}:\tvalue:{value}')

# use of key() to display all keys of dictionary
all_keys = student.keys()
print(all_keys)
all_keys = list(student.keys()) # all keys within a list
print(all_keys)
all_keys = tuple(student.keys()) # all keys within a tuple
print(all_keys)

# iteration through keys() to display all keys of dictionary
for keys in student.keys():
    print(f'keys: {keys}')

# use of values() to display all values in a dictionary
all_values = student.values()
print(all_values)
all_values = list(student.values())
print(all_values)
all_values = tuple(student.values())
print(all_values)

# iteration through values()
for value in student.values():
    print(f'value: {value}')

# len() to display number of key value pairs in dictionary
print(len(student))
