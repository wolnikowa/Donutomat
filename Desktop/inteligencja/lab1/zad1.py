# a
def prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
print(prime(7))
print(prime(8))

# b

def select_primes(num_list):
    result=[];
    for i in num_list:
        if prime(i)==True:
            result.append(i)
    return result;

print(select_primes([1,2,3,4,5,6,7,8,9,10,11,12]))
print(select_primes([3, 6, 11, 25, 19]))
