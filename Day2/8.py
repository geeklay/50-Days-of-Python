def odd_even(l):
    n = m = 0
    for i in l:
        if(i % 2 == 0 and i > n):
            n=i
        elif(i > m):
            m=i
    return n-m

#Uses sieve of erastothenes... 
def prime_numbers(n):
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j]=False
        
    res = [i for i in range(0,n) if sieve[i]]
    print(res.index(1))
    return res
        

k = odd_even([1,2,4,6])
print(k)
print(prime_numbers(10))

