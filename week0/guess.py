def get_guess():
    guess = input ("Enter a guess: ")
    return guess

def main():
    gues = int(get_guess())
    if gues == 50:
        print("Correct")
    else:
        print("Incorrect")
    print (gues)

main()