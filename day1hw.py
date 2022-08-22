# Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total value 1000.
# Meaning that if the cubed number is over 1000 break the loop.

def cubic_printer(num):
    cube_num = int(num ** 0.5)
    
    for i in range(1, cube_num + 1):
        print(i ** 2)

cubic_printer(1000)

# Exercise #2
# Get first prime numbers up to 100

print(True)

prime_list = []

def prim_num(num):
    
    is_prime = True
    
    for i in range(1,num):
#         print(i)
        
        for j in range(2, i):
#             print(f'i: {i} j: {j} i % j: {i % j}')
            if i % j == 0:
                is_prime = False
                break
        
        if is_prime == True:
            prime_list.append(i)
        else:
            is_prime = True
        
    print(prime_list)
        
        
prim_num(100)

# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, else print seniors

def assign_age():
    age = int(input('What is your age?'))
    
    if age < 18:
        print('kids')
    elif 17 < age < 65:
        print('adults')
    else:
        print('seniors')

# Call the function now that it is written.
assign_age()