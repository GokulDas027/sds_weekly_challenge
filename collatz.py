'''Objective: The collatz sequence of a number n is obtained by dividing n by 2
   if n is even or multiplying n by 3 and adding 1 to the product if n is odd,
   until n reaches 1. (n → n/2 if n is even, n → 3n + 1 if n is odd).
   Find n < 1000000 with the longest collatz sequence. '''


def collatz(num):
    i = 0
    while (num != 1) and (num not in db):
        if num % 2 == 0:
            num = num/2
        else:
            num = num*3+1
        i += 1
        if num in db:
            i += db[num]

    return i


db = {}
r2 = 0
result = 0
large = 0
for n in range(1, 1000001):
    a = collatz(n)
    db[n] = a
    if a > large:
        large = a
        r2 = result
        result = n
print("num with longest collatz : {0}".format(result))
print("number of collatz : {0}".format(db[result]))
print("num with second longest collatz : {0}".format(r2))
print("number of collatz : {0}".format(db[r2]))
