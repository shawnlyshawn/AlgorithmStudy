import sys

n = int(sys.stdin.readline())
fibo = [0, 1]

for i in range(n): #0 ~ 16
    fibo.append(fibo[i] + fibo[i+1])

print(fibo[n])