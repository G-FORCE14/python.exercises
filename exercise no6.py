int=eval(input('Enter any integer:'))
multiples=[int, 2*int, 3*int, 4*int, 5*int]
#the * unpacks all the entities in "multiples" such thet they are printed separately.
print(*multiples, sep='---')