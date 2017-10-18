def primes_to_num(num, inclusive = False, primes = None):
    multiples = set()
    if inclusive:
        num += 1
    if not primes:
        primes = [2]
        x = 2
        while 2 * x <= num:
            multiples.add(2 * x)
            x += 1
    else:
        for prime in primes:
            x = 2
            while prime * x <= num:
                multiples.add(prime * x)
                x += 1
    for i in range(primes[-1], num):
        x = 2
        while i * x <= num:
            multiples.add(i * x)
            x += 1
        if i not in multiples:
            if i not in primes:
                primes.append(i)
    return primes


def is_prime(num):
    for i in range(2, num):
        skip = False
        if num % i == 0:
            return False
    return True
    

def is_palindrome(num):
    return str(num) == str(num)[::-1]
    

def smallest_evenly_divisible(to_num):
    if to_num < 1:
        raise Exception("The number needs to be positive and bigger than 0")
    
    if to_num < 3:
        return to_num
    
    num = to_num
    loop_range = to_num - 1
    
    while True:
        for i in range(loop_range, 1, -1):
            if num % i > 0:
                break
                
            if i == 2:
                return num
            
        num += to_num