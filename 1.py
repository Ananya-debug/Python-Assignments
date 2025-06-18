# Write a prime generator program using only primes and using python loops.

def is_prime(num):
    c=0
    for i in range (1,num+1):
        if num % i == 0:
            c=c+1
    
    if c == 2:
        return True
    else:
        return False

def prime_generator():
    n=2
    while True:
        if is_prime(n):
            yield n
        n=n+1


primes = prime_generator()

n = int(input("Enter a number : "))

print("First ",n," prime numbers : ")
for _ in range(n):
    print(next(primes))



        
        
        
   

