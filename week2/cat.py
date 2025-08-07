#1st variation:
i = 0
while i < 3:
    print("meow") 
    i += 1

#2nd variation:
for _ in range(3):
    print("meow")

#3rd variation:
print("meow\n" * 3, end="")

#4th variation:
while True:
    n = int(input("What's n?"))
    if n > 0 :
        break

for _ in range(n):
    print("meow")

#5th variation:
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()