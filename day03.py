subjects = ["Python", "C++", "Database"]
subjects_string = " / ".join(subjects)
print(subjects_string)

numbers = input("FirstNumber SecondNumber : ").split()
#print(numbers[0] + numbers[1])    # concatenation
print(int(numbers[0]) + int(numbers[1]))    # arithmetic operation

# course = "2024 KEB Bootcamp"
# print(course)
# # list_course = course.split()
# list_course = course.split('B')
# print(list_course)