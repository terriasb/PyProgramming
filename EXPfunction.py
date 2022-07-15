
def exp_function(num, pow):
    result = 1
    for index in range(pow):
        result *= num
    return result


print(exp_function(2, 3))

