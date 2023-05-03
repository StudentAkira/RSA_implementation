import math


def is_prime(p):#2**n-1
    tmp = 4
    count = 0
    while count <= p - 1:
        tmp = (tmp*tmp - 2) % p
        count += 1
        if count >= 10000:return False
        if tmp == 0: return True
    return False


i = 4
p = 2**i-1
i = 10
cond = False
count = 0
limit = 50
while not cond or count < limit:
    i+=1
    p = (2 **  i - 1)
    cond = is_prime(p)
    if cond:
        print(p)
        print(len(str(p)))
        count += 1

