from utils_lib.euler_utils import *

def p01():
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            
    print(sum)
    

def p02():
    value_not_to_exceed = 4 * 10**6
    fibonacci = [1, 2]
    
    i = 1
    while fibonacci[i] <= value_not_to_exceed:
        new_num = fibonacci[i - 1] + fibonacci[i]
        if new_num <= value_not_to_exceed:
            fibonacci.append(new_num)
        else:
            break
        i += 1
    
    sum = 0
    for number in fibonacci:
        if number % 2 == 0:
            sum += number
            
    print(sum)
    

def p03(n):
    biggest_prime = current_prime = 2
    while n != 1:
        result = n % current_prime
        if result == 0:
            n =  int(n / current_prime)
            if current_prime > biggest_prime:
                biggest_prime = current_prime
        else:
            next_prime_search = current_prime + 1
            while not is_prime(next_prime_search):
                next_prime_search += 1
            current_prime = next_prime_search
    
    print(biggest_prime)
    
def p04(digits):
    first_number = eval("1" + "0" * (digits - 1))
    over_digit = eval("1" + "0" * (digits))
    num1 = num2 = first_number
    biggest_palindrome = 0
    while num1 < over_digit:
        while num2 < over_digit:
            product = num1 * num2
            if is_palindrome(product) and product > biggest_palindrome:
                biggest_palindrome = product
            num2 += 1
        num1 += 1
        num2 = first_number
    print(biggest_palindrome)

def p05(to_num):
    print(smallest_evenly_divisible(to_num))

def p06(nums):
    sum_squares = sqr_sum = 0
    for i in range(1, nums + 1):
        sum_squares += i**2
        sqr_sum += i
    sqr_sum **= 2
    diff = sqr_sum - sum_squares
    print(diff)

def p07(prime_num_to_find):
    prime_num = 1
    last_prime = 2
    while prime_num < prime_num_to_find:
        num = last_prime + 1
        while not is_prime(num):
            num += 1
        prime_num += 1
        last_prime = num
    print(last_prime)

def p08(digits, series = None):
    if series is not None and series is not str:
        series = str(series)
    elif series is None:
        series = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace('\n', '')
    biggest_prod = 0
    for i in range(len(series)):
        num_str = series[i:i+digits]
        prod = 1
        for c in list(num_str):
            prod *= int(c)
        if prod > biggest_prod:
            biggest_prod = prod
    print(biggest_prod)
    
def p09():
    # a < b < c. a + b + c = 1000
    result = 1000
    
    # Add one to each to account for the loop
    c_max_value = 997 + 1 # a + b = 1 + 2 = 3
    b_max_value = 499 + 1 # a + c = 1 + 500 = 501
    a_max_value = 332 + 1 # b + c = 333 + 334 = 667
    
    for c in range(3, c_max_value):
        for b in range(2, b_max_value):
            if b > c:
                break
            
            for a in range(1, a_max_value):
                if a > b:
                    break
                    
                if a + b + c == result:
                    if a**2 + b**2 == c**2:
                        print(a * b * c)
                        return

def p10(num = None):
    if num is None:
        num = 2*10**6
    primes = primes_to_num(num)
    total = sum(primes)
    print(total)
    
def p11(grid = None):
    # Setup grid
    if not grid:
        grid = []
        temp_grid = \
"""
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
""".split('\n')
        strs_grid = []
        temp_grid.pop(0)
        temp_grid.pop(-1)
        for line in temp_grid:
            strs_grid.append(line.split(' '))
            
        for row in strs_grid:
            grid.append(list(map(int, row)))
    
    biggest_prod = 0
    for i in range(len(grid)):
        loop_biggest_prod = 0
        for j in range(len(grid[i])):
            
            hor_limit = len(grid)
            ver_limit = len(grid[i])
            
            if j + 1 < ver_limit and j + 2 < ver_limit \
            and j + 3 < ver_limit: 
            
                # Right
                prod_1 = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
                if prod_1 > loop_biggest_prod:
                    loop_biggest_prod = prod_1 
                
                if i + 1 < hor_limit and i + 2 < hor_limit \
                and i + 3 < hor_limit:
                    
                    # Diag right
                    prod_2 = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
                    if prod_2 > loop_biggest_prod:
                        loop_biggest_prod = prod_2
                    
            if i - 3 > 0 and i - 2 > 0 \
            and i - 1 > 0:
                pass

            if i + 1 < hor_limit and i + 2 < hor_limit \
            and i + 3 < hor_limit:
                
                if j - 3 >= 0 and j - 2 >= 0 \
                and j - 1 >= 0:
                    
                    # Diag left
                    prod_3 = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]                    
                    if prod_3 > loop_biggest_prod:
                        loop_biggest_prod = prod_3
                
                # Down
                prod_4 = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
                if prod_4 > loop_biggest_prod:
                    loop_biggest_prod = prod_4
        if loop_biggest_prod > biggest_prod:
            biggest_prod = loop_biggest_prod
                    
    print(biggest_prod)
    
def p12():
    last_num = 1
    terms = [1]
    while len(terms) < 10:
        last_num += 1
        terms.append(terms[-1] + last_num)
    print(terms)