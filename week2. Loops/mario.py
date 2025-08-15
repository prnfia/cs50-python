#1st version:
for _ in range(3):
    print("#")

#2nd version:
def main():
    print_column(3)

def print_column(height):
    print("#n" * height, end = "")

main()

#3rd version:
def main():
    print_square(3)

def print_square(size):
    #For each row in square
    for i in range(size):
        #For each brick in row
        for j in range(size):
            #Print brick
            print("#", end="")
        print()

main()

#4th version:
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()