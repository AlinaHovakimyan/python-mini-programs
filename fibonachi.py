
def FibonacciNumbers(num):
    fibonachiNumbers = []
    first = 1
    second = 1
    sum = 0;
    while (second <= num) :
        fibonachiNumbers.append(first)
        sum = first + second
        first = second
        second = sum
    fibonachiNumbers.append(first)          
    return fibonachiNumbers

def sumOfFibonacciNumbers(num):
    sum = 0
    fibonacciNumbrsList = FibonacciNumbers(num)
    for i in fibonacciNumbrsList:
        sum += i
    return sum

def isFibonacciNumber(num):
    if (FibonacciNumbers(num)[-1] == num):
        return True
    else:
        return False




inputCharacter = input("Hello\nPlease insert number(q to quit)\n")	
try:   	
    while (inputCharacter != "q"):
        num = int(inputCharacter)
        option = int(input("\n\n\ninsert option number\n"
    	               "1____print Fibonacci Numbers In Range\n"
    	               "2____print Sum Of Fibonacci Numbers In Range\n"
    	               "3____Is Fibonacci Number\n"
    	               "4____Insert other number\n"))
        if option == 1:
            print(FibonacciNumbers(num));
        elif option == 2:
            print(sumOfFibonacciNumbers(num)); 
        elif option == 3:
            print(isFibonacciNumber(num));
        elif option == 4:
            inputCharacter = input("Please insert number(q to quit)\n")
        else:
            print("Entered incorrect option")
except ValueError as err:
        print(err)