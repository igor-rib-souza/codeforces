n = int(input())

c = 0

for _ in range(n):
    s = input()
    if s[0] == '+' or s[2] == '+':
        c += 1
    else:
        c -= 1

print(c)