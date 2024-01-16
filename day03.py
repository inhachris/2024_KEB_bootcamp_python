course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course.find('KEB'))
print(course.rfind('KEB'))
print(course.index('KEB'))
print(course.rindex('KEB'))
print(course.find('Inha'))    # -1
print(course.index('Inha'))   # ValueError: substring not found

print(course)
course = course.replace('KEB', 'Inha', 2)
print(course)
print(course.strip())
print(course.strip("!#.*"))

# print(course)
# print(course.replace('KEB', 'Inha'))
# print(course)
# course = course.replace('KEB', 'Inha')
# print(course)