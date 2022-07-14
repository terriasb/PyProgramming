secret_word = "code"
user_response = ""
guess_limit = 3
guess_count = 0
out_of_guesses = False

while user_response != "code" and out_of_guesses != True:
    if guess_count < guess_limit:
        user_response = input("What is the secret word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("NEW LOSER!")
else:
    print("YOU WIN!")