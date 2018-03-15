# The implementation of the McGown algorithm for computing Bernoulli numbers quickly and highly accurate.
#
# Computational details:
#   1. Sieve of Eratosthenes for the prime numbers.
#   2. Computation of the zeta-function over primes.
#   3. The expression of the zeta-function and the Bernoulli numbers.
#   4. The Clausen and von Staudt theorem for computing denominator.
#
# Notice that b(1) = +0.5 which could be essential for the Euler-Maclaurin formula.
#
# Ref. Kevin J. McGown, Computing Bernoulli Numbers Quickly, 2005


from decimal import *
import math

pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286')

def factorial(n):return reduce(lambda a,b:a*b,[1]+range(1,n+1))

# Algorithm for finding all prime numbers up to the given limit known as Sieve of Eratosthenes
def prime_sieve(n):
    prime_list = []
    res = []
    for i in range(2, n+1):
        if i not in prime_list:
            res.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return res

# The general procedure for the McGown algorithm
def b(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0.5
    elif (n-1)%2 == 0:
        return 0
    else:
        K = 2*factorial(n)*1/Decimal((2*pi)**(n))
        
        primes = prime_sieve(n+1)
        d = Decimal(1)
        for p in primes:
            if n%(p-1)==0:
                d *= p
        
        N = math.ceil((K*d)**(Decimal(1.0/(n-1))))
        
        z = Decimal(1) 
        for p in primes:
            if p <= N:
                z *= 1/(1-1/(Decimal(p)**n))
        
        a = (-1)**(n/2+1)*Decimal(d*K*z)
        a = a.to_integral_exact(rounding=ROUND_HALF_EVEN)
        if a == 0:
            a = (-1)**(n/2+1) 
        print(a)    # Print numerator
        print(d)    # Print denominator
        return a/d

n = input()

# Set precision. It allows accurate cumputing up to the 154th Bernoulli number.
if n > 28:
    getcontext().prec = n
    
print(b(n)) # Print n-th Bernoulli number

