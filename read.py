employee_file = open("readfrom.txt", "r")  # r, r+, w, a (read, read&write, write, append)
# is the file readable
# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())  # reads first line
# print(employee_file.readline())  # reads line after the first line
# print(employee_file.readlines())  # makes all the lines into an array
for employee in employee_file.readlines():
    print(employee)
employee_file.close()  # always close the file
