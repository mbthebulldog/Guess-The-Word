import getpass

while True:
    master = getpass.getpass("Pick an extra-secret special word: ")
    master = master.lower()
    if (master.isalpha()):
        break
    elif (not master.isalpha()):
        print("Please, no spaces or special characters.")
    else:
        raise Exception("Input does not match either conditional above.")

print("Now pass to a friend, lover, or literate af pet.")
print("---------")

word = list(master)
length = len(word)
right = list("_" * length)
finished = False

while finished == False:
    guess = input("Guess a letter: ")

    if guess not in master:
      print("Guess again, Bucko!")

    for letter in word:
        if letter == guess:
            index = word.index(guess)
            right[index] = guess
            word[index] = "_"

    print(" ".join(right))

    if list(master) == right:
        print("Chet Youbetcha!")

        again = input("Wanna do it all over again? (y/n): ")

        if again == "y":
            master = input("Pick an extra-secret special word: ")
            print("\n" * 50)
            print("Now pass to a friend, lover, or literate af pet.")
            print("---------")
            word = list(master)
            length = len(word)
            right = list("_" * length)
        else:
            finished = True