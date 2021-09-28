import random

def isPrime(x):
    for i in range(2, (x//2)+1):
        if x%i==0:
            return False
    return True

def primeGenerator():
    string = ""
    for i in range(7):
        x=random.randint(1,9)
        string += str(x)
    number = int(string)

    if number%2==0:
        number+=1

    while True:
        if isPrime(number):
            return number
        number+=2

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

p = primeGenerator()
q = primeGenerator()
e = primeGenerator()**2
n = p*q
r = (p-1)*(q-1)     # Euler's Totient
publicKey = (e,n)

def modularInverse(a,b):
    pass
