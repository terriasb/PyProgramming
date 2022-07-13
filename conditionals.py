
is_male = True
is_tall = False
if is_male and is_tall:  # much easier to understand than ||(or) &&(and) operator
    print("You are a tall male")
elif is_tall:
    print("You are Tall")
elif is_male:
    print("You are not a Male")
elif not (is_tall) and is_male:
    print("Your are not a Tall Male")
else:
    print("You are not tall")


