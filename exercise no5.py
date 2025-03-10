#Ask the user to enter a number. Print out the square of the number, but use the sep optional
#argument to print it out in a full sentence that ends in a period.
num=eval(input('Enter a random number:'))
num_sqr=num**2
print('The square of', num, 'is', num_sqr, '.', sep='')