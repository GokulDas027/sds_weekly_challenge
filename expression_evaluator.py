'''Objective: Write a simple arithmetic expression evaluator.
    Note: Do not use your language’s built-in evaluator.'''


process = ['0']
op = ['0']
operators = {'0': 0, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
exp = input("enter the expression : ") + '0'
for i in exp:
    if i in operators:
        if operators[i] > operators[op[-1]]:
            op.append(i)
        else:
            while operators[i] <= operators[op[-1]] and op[-1] != '0':
                o = op.pop(-1)
                n2 = int(process.pop(-1))
                n1 = int(process.pop(-1))
                if o == '^':
                    a = n1 ** n2
                elif o == '*':
                    a = n1 * n2
                elif o == '/':
                    a = n1 / n2
                elif o == '+':
                    a = n1 + n2
                elif o == '-':
                    a = n1 - n2
                process.append(a)
            op.append(i)
    else:
        process.append(i)
print('solution is : {0}'.format(process[-1]))



