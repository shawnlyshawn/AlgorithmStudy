N = input()

lst = []

ans = 0
for i in range(1, int(N)):
    check = i
    for j in str(i):
        check = check + int(j)
    if check == int(N):
        ans = i
        break

print(ans)