num_1 = float(input("Enter first number: "))
operation = input("Enter operation(+, -, /, *): ")
num_2 = float(input("Get second Number: "))

if operation == "+":
    print(num_1 + num_2)
elif operation == "-":
    print(num_1 - num_2)
elif operation == "/":
    print(num_1 / num_2)
elif operation == "*":
    print(num_1 * num_2)
else:
    print("not a valid operation")

