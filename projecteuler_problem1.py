#Find the sum of all the multiples of 3 or 5 below 1000.

#create a function that takes a threshold as input and calculate the sum of all multiples of 3 and 5 in its range.
def answer(threshold):
    count = 0
    for i in range(0, threshold):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    print('The sum of all multiples of 3 or 5 below', threshold, 'is:', count)

#call the function to get the correct answer 
answer(1000)

