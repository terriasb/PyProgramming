
def exp_function(num, power):
    result = 1
    for index in range(power):
        result *= num
    return result


print(exp_function(2, 3))

