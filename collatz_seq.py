#an implemantetion of the mathematical colletz sequence

def collatz(number):
    #assert: number >= 0 and is an integer
    if(number % 2 == 0): #even number
        print(number // 2)
        return(number // 2)
    elif(number % 2 == 1): #odd number
        print(number * 3 + 1)
        return(number * 3 + 1)
    else:
        print('something went horribly wrong')

number = int(input("Enter a number to start the colletz sequence from: "))
while(number > 1):
    number = collatz(number)
