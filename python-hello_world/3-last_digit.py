import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit
    
if last_digit > 5:
     s = "and is greater than 5"
elif last_digit == 0:
     s = "and is 0"
elif last_digit < 6 and not 0:
     s = "and is less than 6 and not 0"
     

print('Last digit of {} is {} {}'.format(number, last_digit, s))