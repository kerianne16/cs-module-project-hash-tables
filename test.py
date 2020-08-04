def sameFrequency(n1, n2):
    x = 0

    while (n1 > 0):
        if (n1 % 10 == n2):
            x += 1
        n1 = int(n1 / 10)
    return x


print(sameFrequency(123, 456))  # False
print(sameFrequency(123, 321))  # True
sameFrequency(123, 32)  # False
