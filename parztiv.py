def isPrime(num):
    i = 2
    maxLength = i*i
    while(maxLength <= num):
        if(num % i == 0):
        	return False
        i += 1
        maxLength = i * i
    return True

def sumOfPrimeNumbers(num):
    sum = 0
    for i in range(2, num + 1):
        if(isPrime(i)):
            sum += i
    return sum

def primeNumbers(num):
    primeNumbers = []
    for i in range(2, num + 1):
	    if(isPrime(i)):
	        primeNumbers.append(i)
    return primeNumbers


inputCharacter = input("Hello\nPlease insert number(q to quit)\n")	
try:   	
    while (inputCharacter != "q"):
        num = int(inputCharacter)
        option = int(input("\n\n\ninsert option number\n"
    	               "1____print Prime Numbers In Range\n"
    	               "2____print Sum Of Prime Numbers In Range\n"
    	               "3____Is Prime Number\n"
    	               "4____Insert other number\n"))
        if option == 1:
            print(primeNumbers(num));
        elif option == 2:
            print(sumOfPrimeNumbers(num)); 
        elif option == 3:
            print(isPrime(num));
        elif option == 4:
            inputCharacter = input("Please insert number(q to quit)\n")
        else:
            print("Entered incorrect option")
except ValueError as err:
        print(err)