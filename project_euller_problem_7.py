#findprime() function will find what is the seleted prime in primes.
count = 10001
number = 0
def findprime(count):
    isprime = True
    count_check = 2
    global number 
    while count_check <= count:
        isprime = True
        number += 1
        if number != 2 or number != 5:
            while number % 2 == 0 or number % 5 == 0:
                number += 1
        for n in range(2, number-1):
            if number % n == 0:
                isprime = False
                break
        if isprime == True:
                    #print("it`s a prime!")
                    count_check = count_check + 1
    #print('The ' + count + 'th ' + 'prime number is ' + number)       
    print(number)
findprime(count)
