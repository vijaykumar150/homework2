name = input("Hi, What is your Name? ")
print("Hello {}! Let's play a game!".format(name))
while True:
    print("Think of random number from 1 to 100, and I'll try to guess it!")
    start, end, number, count = 0, 101, 0, 0
    while True:
        number = (start + end) // 2;
        count += 1
        guess_correct = input("Is it {}?(yes/no)".format(number)).upper()
        if guess_correct == "YES":
            print("Yeey! I got in {} tries".format(count))
            break
        else:
            number_larger = input("Is the number larger than {}?(yes/no)".format(number)).upper()
            if number_larger == "YES":
                start = number
            else:
                end = number
    play_again = input("Do you want to play more?(yes/no)").upper()
    if play_again == "NO":
        print("Bye-bye")
        quit()

