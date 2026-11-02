import sys

pick = 0

def Fibonacci(values = 5):
    number1 = 0
    number2 = 1
    storage = 0
    numbers = [0, 1]
    values -=2
    while values > 0:
        numbers.append(number1 + number2)
        storage = number2
        number2 += number1
        number1 = storage
        values -= 1
    print(numbers)
    return

def primeCheck(number):
    if number == 2:
        print("PRIME")
        return
    elif number == 1:
        print("NOT PRIME")
    else:
        for i in range(2, number + 1):
            if number / i != int(number / i):
                pass
            elif number / i == 1:
                print("PRIME")
                break
            else:
                print("NOT PRIME")
                break
    return
def primes(number = 0, number2 = 10):
    primes = []
    for i in range(number + 1, number2 + 1):
        if i == 2:
            primes.append(2)
        elif i == 1:
            pass
        else:
            for j in range(2 , i + 1):
                if i / j != int(i / j):
                    pass
                elif i / j == 1:
                    primes.append(i)
                else:
                    break
    return(primes)

def mult(number = 3, length = 3):
    chud = ""
    for i in range(1, length+1):
        chud += f"\n{number} x {i} = {number * i}"
        
    return(chud)
def factorial(number = 1):
    chud = number - 1
    if number == 0:
        return(1)
    else:
        while chud > 0:
            number *= chud
            chud -= 1
        return(number)

def collatz(number):
    chud = 0
    if number <= 0:
        print("NOT SCIENTIFICALLY POSSIBLE!!!")
        return
    else:
        while number != 1:
            if number / 2 == int(number / 2):
                print(f"{number} is equal!")
                print(f"{number} / 2 = {int(number / 2)}")
                number /= 2
                number = int(number)
            else:
                print(f"{number} is odd!")
                print(f"({number} * 3) + 1 = {(number * 3) + 1}")
                number *=3
                number += 1
            chud += 1
        print(f"We've reached 1!\nIt took {chud} steps!")
def exit():
    sys.exit("Thank you for playing")

while True:
    pick = input("\nplease select an option with its number: " \
    "\n1: Fibonacci" \
    "\n2: Check if prime" \
    "\n3: Primes in range" \
    "\n4: Multiplication Table" \
    "\n5: Facotial" \
    "\n6: Collatz" \
    "\n7: Exit" \
    "\n")
    if pick == "1":
        try:
            Fibonacci(int(input("How long should the sequence be? ")))
        except:
            print("NOT SCIENTIFICALLY POSSIBLE!!!")
    elif pick =="2":
        try:
            primeCheck(int(input("Please input an integer ")))
        except:
            print("NOT SCIENTIFICALLY POSSIBLE!!!")
    elif pick =="3":
        try:
            Input1 = int(input("Please input the start of your range "))
            Input2 = int(input("Please input the end of your range "))
            print(primes(Input1, Input2))
        except:
            print("NOT SCIENTIFICALLY POSSIBLE!!!")
    elif pick =="4":
        try:
            Input1 = int(input("Please input your factor? "))
            Input2 = int(input("How long should the tabel be? "))
            print(mult(Input1, Input2))
        except:
            print("NOT SCIENTIFICALLY POSSIBLE!!!")
    elif pick =="5":
        try:
            print(factorial(int(input("Please Input an integer "))))
        except:
            print("NOT SCIENTIFICALLY POSSIBLE!!!")
    elif pick =="6":
        try:
            collatz(int(input("Please Input a posative integer ")))
        except:
            print("NOT SCIENTIFICALLY POSSIBLE!!!")
    elif pick =="7":
        exit()