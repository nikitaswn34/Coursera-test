def list_true(n):
    l1 = [False, False]
    for i in range(2, n+1):
        l1.append(i)
    return l1

def mark_false(bool_list, p):
    l2 = [False] * (len(bool_list))
    #print (bool_list)
    #print (l2)
    for i in range(2, len(bool_list)):
        #print (bool_list[i], i, p)
        #print (bool_list[i]%p)
        if bool_list[i]%p == 0 and bool_list[i] != p:
            l2[i] = False
        else:
            l2[i] = True
    #print (l2)
    return l2

def find_next(bool_list, p):
    for i in range(len(bool_list)):
        if bool_list[i] == True and i > p:
            return i


def prime_from_list(bool_list):
    l3 = []
    for i in range(len(bool_list)):
        if bool_list[i] == True:
            l3.append(i)
    return l3

def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)

def mersenne_number(p):
    return (2**p)-1

def is_prime(number):
    flag = True
    for i in range(2, number):
        if number%i == 0:
            flag = False
            break
    return flag

def get_primes(n_start, n_end):
    list_1 = []
    for j in range(n_start, n_end+1):
        if is_prime(j):
            list_1.append(mersenne_number(j))
    return list_1

print (sieve(10))

print (get_primes(0, 10))
