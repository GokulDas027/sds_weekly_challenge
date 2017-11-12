def collatz(num):
    i = 1
    while num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = num*3+1
        i += 1
    return i


r2 = 0
result = 0
large = 0
for n in range(1, 1000000):
    a = collatz(n)
    if a > large:
        large = a
        r2 = result
        result = n
print("num with longest collatz : {0}".format(result))
print("num with second longest collatz : {0}".format(r2))