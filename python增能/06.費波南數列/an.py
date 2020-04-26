a0 = 1
a1 = 2
an = int(input('請輸入要第幾個數字'))

for i in range(an - 1):

    an = 3 * a1 + 5 * a0 + 1
    a0 = a1
    a1 = an

print(an)