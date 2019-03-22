#NC_T4_PRIMES

"""User inputs a number (e.g 20 or 2000)
Program should print on screen all prime numbers less than or equal to that number
(e.g 2,3,5,7,11,13,17,19)

EXTENSION 1:
Report how long the program took
"""

#DECLARE input_num : INTEGER
#DECLARE isPrime: BOOLEAN
#DECLARE counter: INTEGER
#DECLARE y: INTEGER
#DECLARE Beginning_Time: REAL
#DECLARE End_Time: REAL
#DECLARE Total: REAL

import time

input_num = int(input("Find primes up to what number: "))

Beginning_Time = time.clock()

for counter in range(2, input_num + 1):
#the counter is between the number 2 and between the number the user inputs e.g 2 to 5 (remember python does 1 number
#less so you have to add one)
    isPrime = True
#you create a variable isPrime which is a boolean and you set it to be true at first
    for y in range(2 ,counter):
        #again here you create a for loop within a for loop as this time you want to find the prime numbers up
        #until the numbers within the counter (e.g 2 to 5) so below is where it does the working out of each number
        # and seeing if it is a prime or not
        if counter % y == 0:
            #if the number has a remainder of 0 then it's not a prime number
            # when divided by a number in y e.g 15/2 has a remainder of 1 next y
            # is 3 so 15/3 has a remainder of 0
            isPrime = False
            #if there isn't a remainder of 0 when dividing by each numbers leading up to the number inputted by user
            # then it will be still be set to true
            #otherwise isPrime will be set to False
    if isPrime == True:
        print(counter)

End_Time = time.clock()
Total =  End_Time - Beginning_Time
print("Here is how long it took:", Total)