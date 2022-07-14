def max_num(num_1, num_2, num_3):
    if num_1 >= num_2 and num_1 >= num_3:
        print(str(num_1) + " is the largest number.\n")
    elif num_2 >= num_1 and num_2 >= num_3:
        print(str(num_2))
    else:
        print(str(num_3) + "is the biggest number.\n")


def max_value(num_1, num_2, num_3):
    if num_1 == num_2 and num_1 != num_3:
        return num_1


print(max_value(231, 200, 199))
max_num(231, 200, 100)
