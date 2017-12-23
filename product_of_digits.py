# sds coding challenge week 4
'''' Given an n digit number X and a second number k, write a program that will output the largest
product of k consecutive digits in X. (1 ≤ k ≤ 20)
eg : If X=123456789 and k=3, the largest product will be 7*8*9=504.'''


num = input("enter the number : ")
m = int(input("num of digits to be multiplied : "))
if m < 1:
    m = 1
elif m > 20:
    m = 20

product = 1
temp = 1
i = 1
while i <= m:
    for j in num:
            if (product * int(j)) > temp:
                temp = product * int(j)
                x = j
    product = temp
    num = num.replace(x, '')
    i += 1

print("largest product is ", product)
